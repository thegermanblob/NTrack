""" Module containing all RESTful api actions for Tickets """
from pprint import pprint
from flask.app import Flask
from flask.helpers import make_response, url_for
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from flasgger import swag_from
from flask import json, request, abort, session, Blueprint, redirect, jsonify
from models.Client import Client
from models.Tickets import Tickets
from models.User import User
from models.StatusUpdate import StatusUpdates
from api.v1.views.Index import app_views


#todo add session check function 
@app_views.route('/whoami', strict_slashes=False)
def whoami():
    hi = session.pop('email', None)
    if not hi:
        return redirect(url_for('app_views.login'))
    return hi

@app_views.route('/tickets', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/all_tickets.yml')
def all_tickets():
    """ Returns all tickets """ 
    return Tickets.objects.to_json()

@app_views.route('/ticketsfull', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/ticketsfull.yml')
def tickets_full():
    """ returns all tickets with objs inserted """
    tickets_json = Tickets.objects.to_json()
    pprint(tickets_json)
    tickets = json.loads(tickets_json)
    for ticket in tickets:
        try:
            ticket['client_id'] = json.loads(Client.objects.get(id=str(ticket['client_id']['$oid'])).to_json())
            ticket['created_by'] = json.loads(User.objects.get(id=str(ticket['created_by']['$oid'])).to_json())
        except DoesNotExist:
            abort(404, " Client or user id does not exist ")
        except KeyError:
            pass
        for status in ticket['status_updates']:
            try:
                status['created_by'] = json.loads(User.objects.get(id=str(ticket['created_by']['$oid'])).to_json())

            except DoesNotExist:
                abort(404, " Client or user id does not exist ")
            except KeyError:
                pass
    return jsonify(tickets)

@app_views.route('ticket_full/<ticket_id>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/ticket_full.yml')
def ticket_full(ticket_id):
    """ Returns ticket with ful information """
    try:
        ticket = json.loads(Tickets.objects.get(id=ticket_id).to_json())
    except DoesNotExist:
        abort(404, "Invalid ticket id")
    try:
        ticket['client_id'] = json.loads(Client.objects.get(id=str(ticket['client_id']['$oid'])).to_json())
        ticket['created_by'] = json.loads(User.objects.get(id=str(ticket['created_by']['$oid'])).to_json())
    except DoesNotExist:
        abort(404, " Client or user id does not exist ")
    except KeyError:
        pass
    for status in ticket['status_updates']:
        try:
            user = json.loads(User.objects.get(id=str(ticket['created_by']['_id']['$oid'])).to_json())
            status['created_by'] = user 
        except DoesNotExist:
            abort(404, " Client or user id does not exist ")
        except KeyError:
            pass
    return jsonify(ticket)

@app_views.route('/tickets/<tstatus>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/ticketstatus.yml')
def ticket_status(tstatus):
    """ Returns tickets that match status """
    return Tickets.objects(status=tstatus).to_json()

@app_views.route('/tickets', methods=['POST'], strict_slashes=False)
@swag_from('apidoc/post_ticket.yml')
def post_ticket():
    """ Takes a ticket json and adds it to the Database """
    new = request.get_json()
    if not new:
        abort(404, description="Not a JSON")
    if new['user_id'] is None:
        abort(400, description="User id must be included")

    new.pop('_id', None)
    new['created_by'] = User.objects.get(id=new.pop('user_id', None))
    new = Tickets(**new)
    new.save()
    return (new.to_json())

@app_views.route('/ticket/<ticket_id>', methods=['GET'], strict_slashes=False)
@swag_from('apidoc/get_ticket.yml')
def get_ticket(ticket_id):
    """ gets ticket if it is in the database """
    try:
        instance = Tickets.objects.get(id=ticket_id)
        return instance.to_json()
    except DoesNotExist:
        abort(404, description="Ticket_id does not exist")
    except ValidationError:
        abort(400, description="Invalid Id")



def quickpop(a_dict):
    """ Pops uneeded keys"""
    a_dict.pop('created_at', None)
    a_dict.pop('updated_at', None)
    a_dict.pop('status_updates', None)
    a_dict.pop('client_id', None)
    return a_dict



def st_updates(original, up_dict):
    """ creates the status update doc to be embbeded """
    og_dict = json.loads(original.to_json())
    quickpop(og_dict)
    quickpop(up_dict)
    og_keys = og_dict.keys()
    up_keys = up_dict.keys()
    descrip = up_dict.pop('comment', None)
    status_up_stat = up_dict.pop('status', None)
        
    

    #prepares description for status update
    #up_dict.pop('_id', None)
    #for key, val in up_dict.items():
    #    if descrip:
    #        descrip = descrip + "\nChanged {} : {}".format(key ,val)
    #    else:
    #        descrip = "Changed {} : {}".format(key ,val)

    stat = {}
    if status_up_stat:
        stat['status_change'] = status_up_stat
        #if status_up_stat == 'closed':
            #send email
    stat['created_by'] = User.objects.get(id="616f4c9ff66c2a496d7e5bd3")
    stat['comment'] = descrip
    try:
        original.status = up_dict['status']
    except KeyError:
        pass
    
    original.status_updates.append(StatusUpdates(**stat))
    original.save()  


@app_views.route('/tickets/<ticket_id>', methods=['PUT'], strict_slashes=False)
@swag_from('apidoc/put_ticket.yml') # todo write documentation
def put_ticket(ticket_id):
    """ Updates a ticket """
    try:
        original = Tickets.objects.get(id=ticket_id)        
    except DoesNotExist:
        abort(404, description="Given ticket_id is not found")

    updated = request.get_json()
    if not updated:
        abort(400, description='Given object is not a valid JSON')

    
    st_updates(original, updated)
    return Tickets.objects.get(id=ticket_id).to_json()
