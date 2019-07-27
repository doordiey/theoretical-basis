# DFA算法实现

## 源代码

### IDE：CLion

可识别以abb结尾的ab字符串

```c
#include <stdio.h>
/*
 * - 输入：以文件结束符eof结尾的字符串x，DFA D的开始状态s，接收状态集F，转换函数move。
 * - 输出：如果D接收x，则回答“yes"，否则回答"no"。
 */
int move(int s,char c); //设定相关的转换函数
int main() {
    FILE *fp = NULL;
    char content[255]; //接收文件字符串
    int s[4] = {0,1,2,3}; //有穷状态级[0,1,2,3]
    char wordtable[2] = {'a','b'};//输入字母表[a,b]
    int F[1] = {3};//接收状态集F
    int now;
    int in;
    char c;
    in = 0;//用于判定是否在接收状态集内
    now=0; //设定初始状态
    fp = fopen("../example.txt","r"); //此处注意example.txt文件位置
    while((c=fgetc(fp))!=EOF){ //按字符逐个接收文件字符串，到空时结束循环
        now = move(now,c);
        if(now == -1){  //若move返回值为-1，表示字符串中出现了不存在于输入字母表内的字母
            break;
        }
    }
    for(int i=0;i<1;i++){
        if(now==F[i]){
            printf("yes");
            in++;
        }
    }
    if(in==0){
        printf("no");
    }
    fclose(fp);
    return 0;
}
int move(int s,char c){ //见Chapter_3.md中的DFA例子的转换表
    if(c!='b'&&c!='a'){
        return -1;
    }
    if(c=='a'){
        return 1;
    }
    if(c=='b'){
        if(s==0||s==3){
            return 0;
        }
        if(s==1||s==2){
            return s+1;
        }
    }
}
```

