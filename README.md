### Python

## 尽可能地减少代码行数方便记忆

除非特殊情况不使用变量存储 len(),直接使用 len()获取数组长度
使用时再 import,并且将这两部分当作一个整体来记忆

```python
def getRandom(self) -> int:
    import random
    return random.choice(self.values)
```
