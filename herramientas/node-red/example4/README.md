


```js
// generate random number
var min = 1 ;
var max = 10 ;
var a = Math.floor( Math.random() * (max + 1 - min) ) +
min ;

// set random number to message
msg.payload = a;

// return message
return msg;
```

