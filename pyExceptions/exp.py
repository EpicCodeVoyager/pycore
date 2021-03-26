def say_hi(name):
    raise Exception("IAMERROR")
    #a = 1/0
    return f"Hi! {name}"


def handle_hi(msg):
    print(f"msg is {msg}")
    name = say_hi("bbroy")
    return f"{name} : {msg}"

        #name = "default"
    #return f"{name} : {msg}"


def handle_bye():
    try:
        a = handle_hi("INcoming")
        b = handle_hi("Outgoing.")
        print(f"{a},{b}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("bla blu bup.")


handle_bye()
