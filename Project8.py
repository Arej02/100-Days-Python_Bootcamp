alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceasar(original_text,shift_amount,encode_Decode):
    output_text = ""
    if encode_Decode=="decode":
        shift_amount*=-1
    for i in original_text:
        if i not in alphabet:
            output_text+=i
        else:
            shift_position = alphabet.index(i) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
    print(f"Here is the {encode_Decode}d result:{output_text}")

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text,shift,direction)
    result=input("Enter 'yes' if you want to continue or 'no' if you want to exit").lower()
    if result=="no":
        should_continue=False
        print("GoodBye!")





