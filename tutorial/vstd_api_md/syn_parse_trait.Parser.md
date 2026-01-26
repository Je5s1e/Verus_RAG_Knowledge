<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[parse](index.html)

</div>

# Trait <span class="trait">Parser</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/parse.rs.html#1240-1278" class="src">Source</a>
</span>

</div>

``` rust
pub trait Parser: Sized {
    type Output;

    // Required method
    fn parse2(self, tokens: TokenStream) -> Result<Self::Output>;

    // Provided methods
    fn parse(self, tokens: TokenStream) -> Result<Self::Output> { ... }
    fn parse_str(self, s: &str) -> Result<Self::Output> { ... }
}
```

Expand description

<div class="docblock">

Parser that can parse Rust tokens into a particular syntax tree node.

Refer to the [module documentation](index.html "mod syn::parse") for
details about parsing in Syn.

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.Output" class="section method">

<a href="../../src/syn/parse.rs.html#1241"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Output" class="associatedtype">Output</a>

</div>

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.parse2" class="section method">

<a href="../../src/syn/parse.rs.html#1247"
class="src rightside">Source</a>

#### fn <a href="#tymethod.parse2" class="fn">parse2</a>(self, tokens: <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self::<a href="trait.Parser.html#associatedtype.Output" class="associatedtype"
title="type syn::parse::Parser::Output">Output</a>\>

</div>

<div class="docblock">

Parse a proc-macro2 token stream into the chosen syntax tree node.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the stream, an error is returned.

</div>

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.parse" class="section method">

<a href="../../src/syn/parse.rs.html#1255-1257"
class="src rightside">Source</a>

#### fn <a href="#method.parse" class="fn">parse</a>(self, tokens: <a
href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.TokenStream.html"
class="struct" title="struct proc_macro::TokenStream">TokenStream</a>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self::<a href="trait.Parser.html#associatedtype.Output" class="associatedtype"
title="type syn::parse::Parser::Output">Output</a>\>

</div>

<div class="docblock">

Parse tokens of source code into the chosen syntax tree node.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the stream, an error is returned.

</div>

<div id="method.parse_str" class="section method">

<a href="../../src/syn/parse.rs.html#1268-1270"
class="src rightside">Source</a>

#### fn <a href="#method.parse_str" class="fn">parse_str</a>(self, s: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<Self::<a href="trait.Parser.html#associatedtype.Output" class="associatedtype"
title="type syn::parse::Parser::Output">Output</a>\>

</div>

<div class="docblock">

Parse a string of Rust code into the chosen syntax tree node.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the string, an error is returned.

##### <a href="#hygiene" class="doc-anchor">§</a>Hygiene

Every span in the resulting syntax tree will be set to resolve at the
macro call site.

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Parser-for-F" class="section impl">

<a href="../../src/syn/parse.rs.html#1287-1322"
class="src rightside">Source</a><a href="#impl-Parser-for-F" class="anchor">§</a>

### impl\<F, T\> <a href="trait.Parser.html" class="trait"
title="trait syn::parse::Parser">Parser</a> for F

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\>
<a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Output-1"
class="section associatedtype trait-impl">

<a href="../../src/syn/parse.rs.html#1291"
class="src rightside">Source</a><a href="#associatedtype.Output-1" class="anchor">§</a>

#### type <a href="#associatedtype.Output" class="associatedtype">Output</a> = T

</div>

</div>

</div>

</div>

</div>
