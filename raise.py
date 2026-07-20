#When you used to own exception the used raise
Age=int(input("Enter the age: "))

if Age>18:
    raise ValueError("candidate is not elegible")
print("Candidate is elegible for voting")
#try contain the code that raise and exception
#exceptthat contain code that handle the exception
#else block is execute only if no exception occurs
#finally block always execute whether exception occur or not
#raise you can create your own exception using raise keyword
#if try block raised the exception then except and finally block execute
#if try block not raise exception thenelse and finally block will execute
