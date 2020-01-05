# Shoham SIEM System: Logger
## What it does ?
The logger is server to Siem clients ( right now only Windows client available), clients is sending logs using gRPC and logger save the logs in MongoDB.
The logger need to provide categories for clients, to start sending relevant logs.
To use that code, you must generate new certificate, provide public to logger & clients, but only logger have the private.

## How to use ?
This project was tested on CentOS 7.
1. Install python 3 in your machine
2.  Clone project
3. In MongoC folder, edit files and update the DB address.
4. Run `pip install protoc` to install ProtoBuf, then run:
`protoc --proto_path=ProtoBuf --python_out=ProtoBuf ProtoBuf/evtmanager.proto`
`python -m grpc_tools.protoc -I./ProtoBuf --python_out=ProtoBuf --grpc_python_out=ProtoBuf ProtoBuf/evtmanager.proto`
5.  Run `python3 MainServer.py` and wait to see printing:  *Server is UP !*

##Configure the DB
This project working with MongoDB, and build up to use it.
Please make sure to add default values to DB, you can [download it from here](https://files.fm/u/g4k6pvdu "download it from here") or [from here](https://1drv.ms/u/s!An0OKyeC4HO3gjK9eLfC5Dvx6PDS?e=TF4B27 "from here").

