def TextCalc():
    a = """
      _   _                 _        ____           _            _   _                  _    
    | | | |   __ _   ___  | |__    / ___|   __ _  | |   ___    | | | |   __ _    ___  | | __
    | |_| |  / _` | / __| | '_ \  | |      / _` | | |  / __|   | |_| |  / _` |  / __| | |/ /
    |  _  | | (_| | \__ \ | | | | | |___  | (_| | | | | (__    |  _  | | (_| | | (__  |   < 
    |_| |_|  \__,_| |___/ |_| |_|  \____|  \__,_| |_|  \___|   |_| |_|  \__,_|  \___| |_|\_\

                                        <Matico> https://github.com/MaticoProgramacion
        """
    print(a)

TextCalc()

def CalcHash():
    msg = input("Introduce un mensaje: ")
    result = hash(msg)
    print(result)

CalcHash()