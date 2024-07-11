GSM_7_CHARSET = "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\xC7 ÆæßÉ!\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"

def sms_encoding_length(message):
    # Check if the message contains any characters outside the GSM-7 character set
    if any(char not in GSM_7_CHARSET for char in message):
        encoding = "UCS-2"
        length_bits = len(message.encode('utf-16-be')) * 8
    else:
        encoding = "GSM-7"
        length_bits = len(message) * 7

    return encoding, length_bits
