# axereal2.github.io

[https://axereal.net](https://axereal.net)

## リポジトリ構成

| path | 説明|
|:-:|:-:|
| [_includes/about.html](/_includes/about.html) | Aboutの部分のHTML |
| [_includes/company.html](/_includes/company.html) | 会社概要の部分のHTML |
| [_includes/contact.html](/_includes/contact.html) | お問い合わせの部分のHTML |
| [_includes/footer.html](/_includes/footer.html) | フッター部分のHTML |
| [_includes/head.html](/_includes/head.html) | CSSの読み込みなど |
| [_includes/header.html](/_includes/header.html) | ヘッダー部分のHTML |
| [_includes/navbar.html](/_includes/navbar.html) | ナビゲーションバー部分のHTML |
| [_includes/news.html](/_includes/news.html) | ニュース部分のHTML |
| [_includes/portfolio.html](/_includes/portfolio.html) | スポーツの部分のHTML |
| [_includes/scripts.html](/_includes/scripts.html) | JSの読み込みなど |
| [_includes/services.html](/_includes/services.html) | 事業内容の部分のHTML |
| [_includes/sponsor.html](/_includes/sponsor.html) | 協力団体の部分のHTML |
| [_layouts/home.html](/_layouts/home.html) | 大枠。 [_includes/](/_includes/)の中のHTMLを組み合わせて全体を構成する。 |
| [_posts/](/_posts/) | ニュース記事のmarkdownファイルを追加する場所。 |
| [img/posts/](/img/posts/) | ニュース記事に使う画像ファイルを追加する場所。 |

## markdownの文法

### テキスト

#### markdown

```markdown
普通の文章。
```

#### 出力結果

普通の文章。

### 改行

改行したい行の間に空行を入れる。

#### markdown

```markdown
文章1。
(空行)
文章2。
```

#### 出力結果

文章1。

文章2。

### 見出し

#### markdown

```markdown
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
```

#### 出力結果

# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6

### リスト

#### markdown

```markdown
- item1
- item2
- item3

* item1
* item2
* item3

1. item1
2. item2
3. item3

- item1
    - item1-1
    - item1-2
- item2
    - item2-1
    - item2-2
```

#### 出力結果

- item1
- item2
- item3

* item1
* item2
* item3

1. item1
2. item2
3. item3

- item1
    - item1-1
    - item1-2
- item2
    - item2-1
    - item2-2

### リンク

#### markdown

```markdown
[リンク](http://example.com)
```

#### 出力結果

[リンク](http://example.com)

### テーブル

#### markdown
```markdown
| 左寄せ | 中央 | 右寄せ |
|:-----|:----:|---:|
| テキスト | *テキスト* | **テキスト** |
| テキスト | `テキスト` | テキスト |
```

#### 出力結果

| 左寄せ | 中央 | 右寄せ |
|:-----|:----:|---:|
| テキスト | *テキスト* | **テキスト** |
| テキスト | `テキスト` | テキスト |

### 画像

#### markdown

```markdown
![代替テキスト](https://github.com/favicon.ico "キャプション")
```

#### 出力結果

![代替テキスト](https://github.com/favicon.ico "キャプション")

### 強調

`*`が1つでイタリック、2つで太字、3つでイタリック+太字。

#### markdown

```markdown
*強調したい箇所*

**強調したい箇所**

***強調したい箇所***
```

#### 出力結果

*強調したい箇所*

**強調したい箇所**

***強調したい箇所***

### 打ち消し

#### markdown

```markdown
~~打ち消したい箇所~~
```

#### 出力結果

~~打ち消したい箇所~~

### 注釈

#### markdown

```markdown
説明[^1]

[^1] : 補足
```

#### 出力結果

説明[^1]

[^1] : 補足

### 引用

#### markdown

```markdown
> 引用する文章
> 引用する文章
>
> 引用する文章

> 引用する文章
>> 引用する文章(入れ子)
```

#### 出力結果

> 引用する文章
> 引用する文章
>
> 引用する文章

> 引用する文章
>> 引用する文章(入れ子)

### チェックボックス

#### markdown

```markdown
- [ ] チェックボックス1
- [x] チェックボックス2
```

#### 出力結果

- [ ] チェックボックス1
- [x] チェックボックス2

### 水平線
`*`、`-`、`_`のどれかを3つ以上並べればOK。

#### markdown

```markdown
---
***
___
* * *
```

#### 出力結果

---
***
___

* * *

## Webサイトへのニュースの追加方法
