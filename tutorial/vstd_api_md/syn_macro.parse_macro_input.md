<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">parse_macro_input</span> Copy item path

<span class="sub-heading"><a href="../src/syn/parse_macro_input.rs.html#108-128"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! parse_macro_input {
    ($tokenstream:ident as $ty:ty) => { ... };
    ($tokenstream:ident with $parser:path) => { ... };
    ($tokenstream:ident) => { ... };
}
```

Expand description

<div class="docblock">

Parse the input TokenStream of a macro, triggering a compile error if
the tokens fail to parse.

Refer to the [`parse` module](parse/index.html "mod syn::parse")
documentation for more details about parsing in Syn.

  

## <a href="#intended-usage" class="doc-anchor">§</a>Intended usage

This macro must be called from a function that returns
`proc_macro::TokenStream`. Usually this will be your proc macro entry
point, the function that has the \#\[proc_macro\] /
\#\[proc_macro_derive\] / \#\[proc_macro_attribute\] attribute.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::{parse_macro_input, Result};
use syn::parse::{Parse, ParseStream};

struct MyMacroInput {
    /* ... */
}

impl Parse for MyMacroInput {
    fn parse(input: ParseStream) -> Result<Self> {
        /* ... */
    }
}

#[proc_macro]
pub fn my_macro(tokens: TokenStream) -> TokenStream {
    let input = parse_macro_input!(tokens as MyMacroInput);

    /* ... */
}
```

</div>

  

## <a href="#usage-with-parser" class="doc-anchor">§</a>Usage with Parser

This macro can also be used with the [`Parser`
trait](parse/trait.Parser.html "trait syn::parse::Parser") for types
that have multiple ways that they can be parsed.

<div class="example-wrap">

``` rust
impl MyMacroInput {
    fn parse_alternate(input: ParseStream) -> Result<Self> {
        /* ... */
    }
}

#[proc_macro]
pub fn my_macro(tokens: TokenStream) -> TokenStream {
    let input = parse_macro_input!(tokens with MyMacroInput::parse_alternate);

    /* ... */
}
```

</div>

  

## <a href="#expansion" class="doc-anchor">§</a>Expansion

`parse_macro_input!($variable as $Type)` expands to something like:

<div class="example-wrap">

``` rust
match syn::parse::<$Type>($variable) {
    Ok(syntax_tree) => syntax_tree,
    Err(err) => return proc_macro::TokenStream::from(err.to_compile_error()),
}
```

</div>

</div>

</div>

</div>
