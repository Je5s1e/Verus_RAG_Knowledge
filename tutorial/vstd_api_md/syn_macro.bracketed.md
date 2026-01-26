<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">bracketed</span> Copy item path

<span class="sub-heading"><a href="../src/syn/group.rs.html#281-294" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! bracketed {
    ($content:ident in $cursor:expr) => { ... };
}
```

Expand description

<div class="docblock">

Parse a set of square brackets and expose their content to subsequent
parsers.

## <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use proc_macro2::TokenStream;
use syn::{bracketed, token, Result, Token};
use syn::parse::{Parse, ParseStream};

// Parse an outer attribute like:
//
//     #[repr(C, packed)]
struct OuterAttribute {
    pound_token: Token![#],
    bracket_token: token::Bracket,
    content: TokenStream,
}

impl Parse for OuterAttribute {
    fn parse(input: ParseStream) -> Result<Self> {
        let content;
        Ok(OuterAttribute {
            pound_token: input.parse()?,
            bracket_token: bracketed!(content in input),
            content: content.parse()?,
        })
    }
}
```

</div>

</div>

</div>

</div>
