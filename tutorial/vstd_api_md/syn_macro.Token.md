<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">Token</span> Copy item path

<span class="sub-heading"><a href="../src/syn/token.rs.html#871-972" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! Token {
    [abstract] => { ... };
    [as] => { ... };
    [async] => { ... };
    [auto] => { ... };
    [await] => { ... };
    [become] => { ... };
    [box] => { ... };
    [break] => { ... };
    [const] => { ... };
    [continue] => { ... };
    [crate] => { ... };
    [default] => { ... };
    [do] => { ... };
    [dyn] => { ... };
    [else] => { ... };
    [enum] => { ... };
    [extern] => { ... };
    [final] => { ... };
    [fn] => { ... };
    [for] => { ... };
    [if] => { ... };
    [impl] => { ... };
    [in] => { ... };
    [let] => { ... };
    [loop] => { ... };
    [macro] => { ... };
    [match] => { ... };
    [mod] => { ... };
    [move] => { ... };
    [mut] => { ... };
    [override] => { ... };
    [priv] => { ... };
    [pub] => { ... };
    [raw] => { ... };
    [ref] => { ... };
    [return] => { ... };
    [Self] => { ... };
    [self] => { ... };
    [static] => { ... };
    [struct] => { ... };
    [super] => { ... };
    [trait] => { ... };
    [try] => { ... };
    [type] => { ... };
    [typeof] => { ... };
    [union] => { ... };
    [unsafe] => { ... };
    [unsized] => { ... };
    [use] => { ... };
    [virtual] => { ... };
    [where] => { ... };
    [while] => { ... };
    [yield] => { ... };
    [&] => { ... };
    [&&] => { ... };
    [&=] => { ... };
    [@] => { ... };
    [^] => { ... };
    [^=] => { ... };
    [:] => { ... };
    [,] => { ... };
    [$] => { ... };
    [.] => { ... };
    [..] => { ... };
    [...] => { ... };
    [..=] => { ... };
    [=] => { ... };
    [==] => { ... };
    [=>] => { ... };
    [>=] => { ... };
    [>] => { ... };
    [<-] => { ... };
    [<=] => { ... };
    [<] => { ... };
    [-] => { ... };
    [-=] => { ... };
    [!=] => { ... };
    [!] => { ... };
    [|] => { ... };
    [|=] => { ... };
    [||] => { ... };
    [::] => { ... };
    [%] => { ... };
    [%=] => { ... };
    [+] => { ... };
    [+=] => { ... };
    [#] => { ... };
    [?] => { ... };
    [->] => { ... };
    [;] => { ... };
    [<<] => { ... };
    [<<=] => { ... };
    [>>] => { ... };
    [>>=] => { ... };
    [/] => { ... };
    [/=] => { ... };
    [*] => { ... };
    [*=] => { ... };
    [~] => { ... };
    [_] => { ... };
}
```

Expand description

<div class="docblock">

A type-macro that expands to the name of the Rust type representation of
a given token.

As a type, `Token!` is commonly used in the type of struct fields, the
type of a `let` statement, or in turbofish for a `parse` function.

<div class="example-wrap">

``` rust
use syn::{Ident, Token};
use syn::parse::{Parse, ParseStream, Result};

// `struct Foo;`
pub struct UnitStruct {
    struct_token: Token![struct],
    ident: Ident,
    semi_token: Token![;],
}

impl Parse for UnitStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        let struct_token: Token![struct] = input.parse()?;
        let ident: Ident = input.parse()?;
        let semi_token = input.parse::<Token![;]>()?;
        Ok(UnitStruct { struct_token, ident, semi_token })
    }
}
```

</div>

As an expression, `Token!` is used for peeking tokens or instantiating
tokens from a span.

<div class="example-wrap">

``` rust
fn make_unit_struct(name: Ident) -> UnitStruct {
    let span = name.span();
    UnitStruct {
        struct_token: Token![struct](span),
        ident: name,
        semi_token: Token![;](span),
    }
}

if input.peek(Token![struct]) {
    let unit_struct: UnitStruct = input.parse()?;
    /* ... */
}
```

</div>

See the [token module](token/index.html "mod syn::token") documentation
for details and examples.

</div>

</div>

</div>
