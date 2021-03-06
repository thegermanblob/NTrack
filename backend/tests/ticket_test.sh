#!/usr/bin/env bash
curl -X GET http://192.168.1.148:5000/api/v1/tickets;
curl -X GET http://192.168.1.148:5000/api/v1/tickets/open;
curl -X GET http://192.168.1.148:5000/api/v1/tickets/closed;
curl -X POST http://192.168.1.148:5000/api/v1/tickets/ -H "Content-Type: application/json" -d '{ "status": "open", "status_updates": [], "client_id": { "$oid": "616483c079e32de906afab6a" }}';
curl -X GET http://192.168.1.148:5000/api/v1/ticket/616dadfb29513e64c52dc755;
curl -X PUT http://192.168.1.148:5000/api/v1/tickets/616dadfb29513e64c52dc755 -H "Content-Type: application/json" -d '{ "status":"closed" }';
curl -X PUT http://192.168.1.148:5000/api/v1/tickets/616dadfb29513e64c52dc755 -H "Content-Type: application/json" -d '{"pepito":"p"}';
curl -X GET http://192.168.1.148:5000/api/v1/client/616483c079e32de906afab6a;
curl -X GET http://192.168.1.148:5000/api/v1/clients;
curl -X POST http://192.168.1.148:5000/api/v1/clients/ -H "Content-Type: application/json" -d '{"name":"bob", "last_name":"El constructor", "email":"bobsconstruction@emaiasl.com"}';
curl -X PUT http://192.168.1.148:5000/api/v1/clients/616483c079e32de906afab6a -H "Content-Type: application/json" -d '{"name":"barneyeldinow"}';
curl -X PUT http://192.168.1.148:5000/api/v1/clients/616483c079e32de906afab6a -H "Content-Type: application/json" -d '{"name":"barneyeldinow", "non":"bob"}';

{ "status": "open", "status_updates": [], "client_id": { "$oid": "6170be1ace938dab7b685232" }}