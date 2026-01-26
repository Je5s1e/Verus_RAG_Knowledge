<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">parenthesized</span> Copy item path

<span class="sub-heading"><a href="../src/syn/group.rs.html#146-159" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! parenthesized {
    ($content:ident in $cursor:expr) => { ... };
}
```

Expand description

<div class="docblock">

Parse a set of parentheses and expose their content to subsequent
parsers.

## <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parenthesized, token, Ident, Result, Token, Type};
use syn::parse::{Parse, ParseStream};
use syn::punctuated::Punctuated;

// Parse a simplified tuple struct syntax like:
//
//     struct S(A, B);
struct TupleStruct {
    struct_token: Token![struct],
    ident: Ident,
    paren_token: token::Paren,
    fields: Punctuated<Type, Token![,]>,
    semi_token: Token![;],
}

impl Parse for TupleStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        let content;
        Ok(TupleStruct {
            struct_token: input.parse()?,
            ident: input.parse()?,
            paren_token: parenthesized!(content in input),
            fields: content.parse_terminated(Type::parse, Token![,])?,
            semi_token: input.parse()?,
        })
    }
}
```

</div>

</div>

</div>

</div>
