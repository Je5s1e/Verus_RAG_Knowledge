<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">parse_quote_spanned</span> Copy item path

<span class="sub-heading"><a href="../src/syn/parse_quote.rs.html#112-116" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! parse_quote_spanned {
    ($span:expr=> $($tt:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

This macro is
[`parse_quote!`](macro.parse_quote.html "macro syn::parse_quote") +
[`quote_spanned!`](../quote/macro.quote_spanned.html "macro quote::quote_spanned").

Please refer to each of their documentation.

## <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use quote::{quote, quote_spanned};
use syn::spanned::Spanned;
use syn::{parse_quote_spanned, ReturnType, Signature};

// Changes `fn()` to `fn() -> Pin<Box<dyn Future<Output = ()>>>`,
// and `fn() -> T` to `fn() -> Pin<Box<dyn Future<Output = T>>>`,
// without introducing any call_site() spans.
fn make_ret_pinned_future(sig: &mut Signature) {
    let ret = match &sig.output {
        ReturnType::Default => quote_spanned!(sig.paren_token.span=> ()),
        ReturnType::Type(_, ret) => quote!(#ret),
    };
    sig.output = parse_quote_spanned! {ret.span()=>
        -> ::core::pin::Pin<::alloc::boxed::Box<dyn ::core::future::Future<Output = #ret>>>
    };
}
```

</div>

</div>

</div>

</div>
