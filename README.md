# Problem I want to solve 

解决当文件标题/内容里符合相关文字时，自动打上标签，之后可以自动移到制定的位置

## filter file

- define
  - tag name
  - list of string / regex

example:

```yaml
a:
  - aa
  - bb
```

```
from Filter.GeneralFilter import GeneralFilter
general_filter = GeneralFilter(f"{PATH}/filter_file/bqb.yaml")
```

## mover class

- base folder
- tag and folder mapping?
- move function (tag, file) 

```
from Mover.FileMover import FileMover
mover = FileMover(path="xxx")
```