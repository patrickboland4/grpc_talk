---?image=assets/images/grpc.jpg&size=cover&opacity=10&position=left

## better services
#### with 
## gRPC
#### and
## Protocol Buffers

---

## this talk is about how computers communicate

---

### where I am coming from

[//]: <> (this is a comment, insert image of bladerunner)

---

### where we are headed

- context
- why, how, what of the subject
- demo
- q & a

---

what is an @size[3em](rpc) anyway?

- @size[3em](r)emote @size[3em](p)rocedure @size[3em](c)all
    - program requests a service in another computer as if it is local
    - abstracts concerns

---

### rpcs are a mechanism by which computers communicate

---

### why 
we really need great communication

- robust, performant services
- happy customers
- high developer quality of life

---

### how
this will be achieved

- simple, performant communication protocol
- machine readable api contracts
- multiple language support @size[.5em](code generators)
- easy to use

---

### what
# REST

---

# The End
### THANK YOU

---

### so why not REST? 
- REST has a lot going for it
- building client apis is unsustainable (lanugage support)

---

### what
will actually make this work

- gRPC 
    - Google Remote Procedure Call
    - open source, universal, high performance rpc framework
    - started and maintained by Google

---

### how gRPC works

- a **service defition** describes the api
- client and server code is generated from **service definition** in **10+ languages**
- messages encoded into **protocol buffers**
- make a unary or streaming connection
- use / federate a service

---

### gRPC compared to REST

performance over http2 protocol
binary format serialization
bidirectional streaming
protocol buffers vs JSON
machine readable api contracts
