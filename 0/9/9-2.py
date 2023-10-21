morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
def solution(letter):
    letters = letter.split(' ')
    answer = []
    for i in letters:
        answer.append(morse[i])
    return ''.join(answer)

# 또 다른 풀이
def solution2(letter):
    return ''.join([morse[i] for i in letter.split(' ')])

def solution3(letter):
    answer = ''
    letter = letter.split(' ')
    for i in letter:
        answer += morse[i]
    return answer
