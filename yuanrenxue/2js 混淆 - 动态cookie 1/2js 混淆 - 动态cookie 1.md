# 一.分析
这个题目为动态cookie生成，那么直接寻找js生成位置即可

先用Python请求一下，返回一段js代码，一看就是ob,先把OB的代码解除混淆，ob_en.js

观察 cookies特征为 m=...
然而在生成cookies的时候为  document["cookie"] = "m" + M() + "=" + V(Y) + "|" + Y + "; path=/";
很明显M()，没有返回值，那么判断它做了什么通过代码来看，没有改变全局变量那么直接删除在cookie这的调用即可
进行调用的时候发现程序一直运行不结束，  setInterval(M(), 500); 一直运行这个代码，那这个M函数有什么蹊跷
```

    try {
      if (global) {
        console["log"]("\u4EBA\u751F\u82E6\u77ED\uFF0C\u4F55\u5FC5python\uFF1F");
      } else {
        while (1) {
          console["log"]("\u4EBA\u751F\u82E6\u77ED\uFF0C\u4F55\u5FC5python\uFF1F");
          debugger;
        }
      }
    } catch (a3) {
      return navigator["vendorSub"];
    }
```
于是把函数里面的函数体全部删除了，但是报QZ没被定义，又看了一下QZ并不是外部变量，那么只有一种可能eval执行,但是在浏览器中看eval执行的代码，除了挤压堆栈之外没什么操作，也直接删除掉，直接把Qz提到外面完全删除M()函数。完事
上方这个坑爹的代码,因为node有global对象，它就会进去，然后返回navigator["vendorSub"]，进行报错，但是我看到else里面的代码之后，是个debugger但是完全没有在node里面生效，但是在浏览器中也没有生效，有点奇怪他这个逻辑的过程，
但是不用想太多，直接删除即可因为我的目的是要cookies不用管与cookie生成无关的一些代码。

# 二.扣代码
把分析1的多余代码删除掉，构建test函数，返回cookies即可