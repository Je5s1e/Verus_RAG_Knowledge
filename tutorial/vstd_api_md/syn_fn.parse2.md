<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Function <span class="fn">parse2</span> Copy item path

<span class="sub-heading"><a href="../src/syn/lib.rs.html#926-928" class="src">Source</a>
</span>

</div>

``` rust
pub fn parse2<T: Parse>(tokens: TokenStream) -> Result<T>
```

Expand description

<div class="docblock">

Parse a proc-macro2 token stream into the chosen syntax tree node.

This function parses a `proc_macro2::TokenStream` which is commonly
useful when the input comes from a node of the Syn syntax tree, for
example the body tokens of a
[`Macro`](struct.Macro.html "struct syn::Macro") node. When in a
procedural macro parsing the `proc_macro::TokenStream` provided by the
compiler, use [`syn::parse`](fn.parse.html "fn syn::parse") instead.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the stream, an error is returned.

</div>

</div>

</div>
