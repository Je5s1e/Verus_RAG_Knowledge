<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../../index.html)::[parse](../index.html)::[discouraged](index.html)

</div>

# Trait <span class="trait">AnyDelimiter</span> Copy item path

<span class="sub-heading"><a href="../../../src/syn/discouraged.rs.html#205-209"
class="src">Source</a> </span>

</div>

``` rust
pub trait AnyDelimiter {
    // Required method
    fn parse_any_delimiter(
        &self,
    ) -> Result<(Delimiter, DelimSpan, ParseBuffer<'_>)>;
}
```

Expand description

<div class="docblock">

Extensions to the `ParseStream` API to support manipulating invisible
delimiters the same as if they were visible.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.parse_any_delimiter" class="section method">

<a href="../../../src/syn/discouraged.rs.html#208"
class="src rightside">Source</a>

#### fn <a href="#tymethod.parse_any_delimiter"
class="fn">parse_any_delimiter</a>(&self) -\> <a href="../../type.Result.html" class="type"
title="type syn::Result">Result</a>\<(<a href="../../../proc_macro2/enum.Delimiter.html" class="enum"
title="enum proc_macro2::Delimiter">Delimiter</a>, <a href="../../../proc_macro2/extra/struct.DelimSpan.html"
class="struct"
title="struct proc_macro2::extra::DelimSpan">DelimSpan</a>, <a href="../struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'\_\>)\>

</div>

<div class="docblock">

Returns the delimiter, the span of the delimiter token, and the nested
contents for further parsing.

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-AnyDelimiter-for-ParseBuffer%3C'a%3E"
class="section impl">

<a href="../../../src/syn/discouraged.rs.html#211-225"
class="src rightside">Source</a><a href="#impl-AnyDelimiter-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="trait.AnyDelimiter.html" class="trait"
title="trait syn::parse::discouraged::AnyDelimiter">AnyDelimiter</a> for <a href="../struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

</div>

</div>

</div>
