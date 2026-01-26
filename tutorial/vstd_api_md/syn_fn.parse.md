<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Function <span class="fn">parse</span> Copy item path

<span class="sub-heading"><a href="../src/syn/lib.rs.html#908-910" class="src">Source</a>
</span>

</div>

``` rust
pub fn parse<T: Parse>(tokens: TokenStream) -> Result<T>
```

Expand description

<div class="docblock">

Parse tokens of source code into the chosen syntax tree node.

This is preferred over parsing a string because tokens are able to
preserve information about where in the user’s code they were originally
written (the “span” of the token), possibly allowing the compiler to
produce better error messages.

This function parses a `proc_macro::TokenStream` which is the type used
for interop with the compiler in a procedural macro. To parse a
`proc_macro2::TokenStream`, use
[`syn::parse2`](fn.parse2.html "fn syn::parse2") instead.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the stream, an error is returned.

</div>

</div>

</div>
