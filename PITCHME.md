---?image=assets/images/grpc.jpg&size=cover&opacity=10&position=left

## better services
#### with 
## gRPC
#### and
## Protocol Buffers

---

## this talk is about how computers communicate

---?image=assets/images/bladerunner.jpg&size=100%&opacity=70
## where i am coming from
- data platform / engineering team @ BoA
- high performance, federated microservices

[//]: <> (this is a comment, insert image of bladerunner)

---?image=assets/images/harrisonFord1.jpg&size=100%&opacity=70
### where we are headed

- why, how, what of the subject
- demo
- q & a

---

### rpc = @color[gold](remote procedure call)
- program requests a service in another computer as if it is local
- abstracts concerns

Note:

- Dont need to understand network details
- abstracts connection details

---

## stub = @color[pink](native client library)
#### allows client and server to communicate transparently

---

## rpcs are a mechanism by which computers communicate

---

## microservices
#### @color[gold](architectural paradigm)
@ul
- independent service evolution
- narrow service scope, built as needed
- optimized for change and reuse
- generic
@ulend

---

### why 
#### we really need great communication

- robust, performant services
- happy customers
- high developer quality of life

---

### how
#### this will be achieved

- simple, performant communication protocol
- machine readable api contracts
- multiple language support
- easy to use

---

### what

---?image=assets/images/chair.jpg&size=100%&opacity=30
# REST

---

# The End
### THANK YOU

---

### so why not REST? 
@ul[squares]
- REST is probably enough for simple HTTP Services
- GET, POST, PUT, DELETE, REST semantics well understood
- Complex services require more flexibility
- Bank transfer scenario
- Keep client concerns narrow
@ulend

---?image=assets/images/backFuture.jpg&size=100%&opacity=40
### really, though. 
@ul[squares]
- writing client apis requires humans (expensive, grumpy)
- REST is less efficient - streaming issues
- REST (in practice) usually means HTTP endpoints
- no formal machine-readable API conracts
@ulend

---

### how (revisited)
#### this will be achieved

- simple, performant communication protocol
- machine readable api contracts
- multiple language support
- easy to use

---

# @color[#42cbf4](gRPC)

#### will actually make this work

---

# @color[#42cbf4](gRPC)


- Google Remote Procedure Call
- open source, universal, high performance rpc framework
- started and maintained by Google

---

### how @color[#42cbf4](gRPC) works

@ul[squares]
- a **service definition** describes the api
- client and server code is generated from **service definition** in **10+ languages**
- messages encoded into **protocol buffers**
- clients connect and call services
- federated services
@ulend

---?image=assets/images/grpcDesign.svg

---

## @color[gold](protocol buffers)
@ul
- message format & IDL
- small, fast, unambiguous (strongly typed)
- language neutral, platform neutral
- extensible mechanism for serializing structured data
- write once, generate source code
@ulend


---

### gRPC on the wire

- HTTP/2
- protocol buffer serialization (binary protocol)
- clients open a connection to a grpc server
- new HTTP/2 stream for each RPC call
- allows client-side and server-side streaming

---

gRPC | REST
--- | ---
HTTP2.0 | HTTP1.1
binary protocol | text protocol
bidirectional streaming | unary
machine readable api contracts | no formal contract
code generators for 10+ languages | build client api per language
gRPC = protocol buffers + HTTP2 | REST = JSON + HTTP1

---

## pb vs other forms of marshalling
@ul
- pickle
    - python specific, no schema evolution
- string / json
    - encoding decoding runtime costs, heavy
- xml
    - complicated, inefficient, unreadable
@ulend

---

### gRPC answers these questions in @color[gold](10+ languages)

1. how does one expose a service on a remote machine?
2. how does a client call a service on a remote machine?
3. how is data serialized / deserialized over the wire?
4. what is the nature of the call?
5. authentication?

--- 

# demo

---

### gRPC shortcomings

- need to adapt to gRPC style, generated code

---

## takeaways

- machine readable api contracts are awesome
- implement server code once, many client apis for free
- flexible, composable, generic
- ideal for microservice architecture

--- 

## soap box
- embrace great services, allow others to also embrace them @color[pink](without concern)
- don't corner your service into a language
- flexible, reusable, generic wins

---

# @color[gold](Thank you)
#### github.com/patrickboland4/grpc_talk
#### patrickboland4@gmail.com
