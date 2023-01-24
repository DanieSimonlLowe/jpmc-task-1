# used to test the client.
import client as c
import sys



def makeQuote(name, bid_price,ask_price):
    rect = dict()
    top_bid = dict()
    
    top_bid["price"] = bid_price;
    top_ask = dict()
    top_ask["price"] = ask_price;    
    
    rect["stock"] = name
    rect["top_bid"] = top_bid;
    rect["top_ask"] = top_ask;
    return rect


def largeNumQouteGetPoint():
    diff = sys.maxsize/1000
    stock, bid_price, ask_price, price = c.getDataPoint(makeQuote("s", sys.maxsize,2*sys.maxsize))
    if (stock != "s"):
        print("largeNumQouteGetPoint failed at stock name")
        return False
    elif (bid_price < sys.maxsize-diff or bid_price > sys.maxsize+diff):
        print(f"largeNumQouteGetPoint failed at bid price of :{bid_price}")
        return False
    elif (ask_price < 2*sys.maxsize-diff or ask_price > 2*sys.maxsize+diff):
        print(f"largeNumQouteGetPoint failed at ask price of :{ask_price}")
        return False
    elif (price < 1.5*sys.maxsize-diff or price > 1.5*sys.maxsize+diff):
        print(f"largeNumQouteGetPoint failed at price of {price}")
        return False    
    return True

def largeDiffQouteGetPoint():
    diff = sys.maxsize/1000
    stock, bid_price, ask_price, price = c.getDataPoint(makeQuote("s", 0.1,2*sys.maxsize))
    if (stock != "s"):
        print("largeDiffQouteGetPoint failed at stock name")
        return False
    elif (bid_price < 0.1-0.001 or bid_price > 0.1+0.001):
        print(f"largeDiffQouteGetPoint failed at bid price of :{bid_price}")
        return False
    elif (ask_price < 2*sys.maxsize-diff or ask_price > 2*sys.maxsize+diff):
        print(f"largeDiffQouteGetPoint failed at ask price of :{ask_price}")
        return False
    elif (price < 1*sys.maxsize-diff or price > 1*sys.maxsize+diff):
        print("largeDiffQouteGetPoint failed at bid price")
        return False    
    return True

def normalQouteGetPoint():
    stock, bid_price, ask_price, price = c.getDataPoint(makeQuote("stuff", 1,2))
    diff = 0.1
    
    if (stock != "stuff"):
        print("normalQouteGetPoint failed at stock name")
        return False
    elif (bid_price != 1):
        print("normalQouteGetPoint failed at bid price")
        return False
    elif (ask_price != 2):
        print("normalQouteGetPoint failed at ask price")
        return False
    elif (price < 1.5-diff or price > 1.5+diff):
        print("normalQouteGetPoint failed at price")
        return False    
    return True
def noDiffQouteGetPoint():
    diff = 1/1000
    stock, bid_price, ask_price, price = c.getDataPoint(makeQuote("objects", 2, 2))
    if (stock != "objects"):
        print("noDiffQouteGetPoint failed at stock name")
        return False
    elif (bid_price < 2-0.001 or bid_price > 2+0.001):
        print(f"noDiffQouteGetPoint failed at bid price of :{bid_price}")
        return False
    elif (ask_price < 2-diff or ask_price > 2+diff):
        print(f"noDiffQouteGetPoint failed at ask price of :{ask_price}")
        return False
    elif (price < 2-diff or price > 2+diff):
        print("noDiffQouteGetPoint failed at price")
        return False    
    return True

def smallNumQouteGetPoint():
    num = 1/sys.maxsize
    diff = num/10
    
    stock, bid_price, ask_price, price = c.getDataPoint(makeQuote("objects", num, 5*num))
    if (stock != "objects"):
        print("smallNumQouteGetPoint failed at stock name")
        return False
    elif (bid_price < num-0.001 or bid_price > num+0.001):
        print(f"smallNumQouteGetPoint failed at bid price of :{bid_price}")
        return False
    elif (ask_price < 5*num-diff or ask_price > 5*num+diff):
        print(f"smallNumQouteGetPoint failed at ask price of :{ask_price}")
        return False
    elif (price < 3*num-diff or price > 3*num+diff):
        print(f"smallNumQouteGetPoint failed at price of {price} not {3*num}")
        return False    
    return True


def ratioCheck():
    nums = [1,20,600,163212312,0.0001,sys.maxsize,sys.maxsize*100,1/sys.maxsize,6/sys.maxsize]
    for n in nums:
        for m in nums:
            if c.getRatio(n,m) != n/m:
                print(f"ratio function failed for {n} and {m}")
                return False
    return True

def main():
    
    normalQouteGetPoint()
    largeNumQouteGetPoint()
    largeDiffQouteGetPoint()
    noDiffQouteGetPoint()
    smallNumQouteGetPoint()
    ratioCheck()
    print("all tests passed")
    
    
main()