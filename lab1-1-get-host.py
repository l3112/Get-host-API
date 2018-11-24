"""""
#I'm using Mac OS so.
"""""

python3 lab1-1-get-host.py
""""'activate python3 and get the code""""""'

from apicem import *
"""""is that what we did yesterday""""

def get_host()
"""""This is a function. It makes a list of every host we can see"""""
host_list[]
try:
  resp = get(api="host")
      #get from request module in apicem.py
     response_json = resp.json()
     print ("Stat: ",resp.status_code)
  """" seems like a variable that changes based upon status"""""
     print (json.dumps(response_json,indent=4))
 """"converted to JSON formatted string""""
     except:
        print ("Something is wrong with GET /host! req!")
        return host_list
        i=0
     """ variable i is 0?""""
     for item in response_json["response"]:
     i+=1
     """"it's now number + 1""""
     host_list.append([i,item["hostIP"],item["hostType"],item["connectedNetDevIP"]])
     return host_list
     
     if __name__ == "__main__": # 
          host=get_host()
     print (tabulate(host,headers=['number','host IP','type','connected to network device'],tablefmt="rst"))   
