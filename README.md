# Submission for Code 100 Twillio Challenge

## Test Result
```
message = "Ahoy World"
encoding, length_bits = sms_encoding_length(message)
print(f"Encoding: {encoding}")
print(f"Length in bits: {length_bits}")
```
Encoding: GSM-7 <br />
Length in bits: 70

```
message = "This is a test message with special characters: ñáéíóú"
encoding, length_bits = sms_encoding_length(message)
print(f"Encoding: {encoding}")
print(f"Length in bits: {length_bits}")
```
Encoding: UCS-2 <br />
Length in bits: 864

```
message = "Visit the Twilio booth at Hall A 03 during WeAreDeveloper World Congress"
encoding, length_bits = sms_encoding_length(message)
print(f"Encoding: {encoding}")
print(f"Length in bits: {length_bits}")
```
Encoding: GSM-7 <br />
Length in bits: 504

```
message = "Rumors say Twilio will provide healthy smoothies 🥤🍓🍍"
encoding, length_bits = sms_encoding_length(message)
print(f"Encoding: {encoding}")
print(f"Length in bits: {length_bits}")
```
Encoding: UCS-2 <br />
Length in bits: 880

## Notes
My test results for the USC-2 length in bits are different with testset result provided [here](https://puzzles.code100.dev/code100/puzzles/twilio-vip/dataset.json) but same as [message segment calculator](https://twiliodeved.github.io/message-segment-calculator/)
