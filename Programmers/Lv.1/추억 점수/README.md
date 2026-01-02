# `||`와 `??`의 차이점

## `||` (논리 OR)
```javascript
    a || b
```
-> a가 **falsy**인 경우 b 사용.

### **falsy?**
```javascript
false
0
''
null
undefined
NaN
```


## `??` (Nullish Coalescing)
```javascript
a ?? b
```
-> a가 `null` 또는 `undefined` 일 때만 b 사용. <br/>
즉, 진짜 값이 없을 때만(정의 안 됐을 때만) 0을 사용함

