# Simple Dynamic Python API Server
A simple an dynamic solution to creating user friendly APIs in python

By: [Mr_ShoeShoe66](https://github.com/MrShoeShoe66) on github.
Also known as mrshoe_ on Discord.

## How To Use

The program is designed to be a simplistic as it can be with suport for nested folders and routes along with persistant api state.

### Example File

Here is a example of how a file will look:

```py
from classes.route import RouteClass

def executeAPICall(type, prams, apiState, externalSelf):
    return {"success": True}

route = RouteClass(executeAPICall)
```

#### How To Use
The externalSelf is for grabbing more data not nicely formatted as its a direct reference to the original http request self variable


For the API State its obviouse, its the 3rd varyable being the API's data which is in the format of a JSON object

Prams is another dictionary object as is used to pass paramiters from the client to server like this: `prams["key name"]`

The type varyable is simply the type of http request, think GET, SET, POST, etc.



### Error Files

Here are all ther error files and info about them

| File Name     |   Error                 | HTTP Error Code | Error Side |
|:--------------|:------------------------|:----------------|:-----------|
| badAccess.py  |  Bad Authentication     |      403        |   Client   |
| notAllowed.py |  No Authentication      |      403        |   Client   |
| notFound.py   |  File Not Found         |      404        |   Client   |
| badGate.py    |  Gateway Error          |      502        |   Server   |
| compute.py    |  Fail to Process Reuest |      500        |   Server   |

#### Example Error File & Usage

```py
from classes.error import * 

def compErr(errData):
    return {"err":"The requested resource was not found."}

comp = errorClass(404, compErr)
```

This one is much more simplistic with the errData being the raised exeption from the code

### Config Files

To configure the coe simply use the `./settings.conf` file

For the conf file use `#`s for comments and here are the options

| Config Name | Value Type | Default Value |
|-------------|------------|---------------|
| password    |   String   |               |
| keys        |   Boolean  |   False       |
| port        |   Int      |   80          |