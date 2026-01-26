<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Trait <span class="trait">MacroResult</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/lib.rs.html#2466-2491"
class="src">Source</a> </span>

</div>

``` rust
pub trait MacroResult {
    // Required method
    fn into_result(self) -> Result<TokenStream>;

    // Provided method
    fn into_stream(self) -> TokenStream
       where Self: Sized { ... }
}
```

Expand description

<div class="docblock">

Helper trait describing values which may be returned by macro
implementation methods used by this crate’s macros.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.into_result" class="section method">

<a href="../src/synstructure/lib.rs.html#2468"
class="src rightside">Source</a>

#### fn <a href="#tymethod.into_result" class="fn">into_result</a>(self) -\> <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>\>

</div>

<div class="docblock">

Convert this result into a `Result` for further processing / validation.

</div>

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.into_stream" class="section method">

<a href="../src/synstructure/lib.rs.html#2482-2490"
class="src rightside">Source</a>

#### fn <a href="#method.into_stream" class="fn">into_stream</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.TokenStream.html"
class="struct" title="struct proc_macro::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert this result into a `proc_macro::TokenStream`, ready to return
from a native `proc_macro` implementation.

If `into_result()` would return an `Err`, this method should instead
generate a `compile_error!` invocation to nicely report the error.

*This method is available if `synstructure` is built with the
`"proc-macro"` feature.*

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-MacroResult-for-TokenStream" class="section impl">

<a href="../src/synstructure/lib.rs.html#2507-2511"
class="src rightside">Source</a><a href="#impl-MacroResult-for-TokenStream" class="anchor">§</a>

### impl <a href="trait.MacroResult.html" class="trait"
title="trait synstructure::MacroResult">MacroResult</a> for <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.into_result" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#2508-2510"
class="src rightside">Source</a><a href="#method.into_result" class="anchor">§</a>

#### fn <a href="#tymethod.into_result" class="fn">into_result</a>(self) -\> <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>\>

</div>

</div>

<div id="impl-MacroResult-for-TokenStream-1" class="section impl">

<a href="../src/synstructure/lib.rs.html#2497-2505"
class="src rightside">Source</a><a href="#impl-MacroResult-for-TokenStream-1" class="anchor">§</a>

### impl <a href="trait.MacroResult.html" class="trait"
title="trait synstructure::MacroResult">MacroResult</a> for <a
href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.TokenStream.html"
class="struct" title="struct proc_macro::TokenStream">TokenStream</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **not (WebAssembly and (`target_os=unknown` or WASI)) and
crate feature `proc-macro`** only.

</div>

</div>

<div class="impl-items">

<div id="method.into_result-1" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#2498-2500"
class="src rightside">Source</a><a href="#method.into_result-1" class="anchor">§</a>

#### fn <a href="#tymethod.into_result" class="fn">into_result</a>(self) -\> <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>\>

</div>

<div id="method.into_stream-1" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#2502-2504"
class="src rightside">Source</a><a href="#method.into_stream-1" class="anchor">§</a>

#### fn <a href="#method.into_stream" class="fn">into_stream</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.TokenStream.html"
class="struct" title="struct proc_macro::TokenStream">TokenStream</a>

</div>

</div>

<div id="impl-MacroResult-for-Result%3CT,+Error%3E"
class="section impl">

<a href="../src/synstructure/lib.rs.html#2513-2520"
class="src rightside">Source</a><a href="#impl-MacroResult-for-Result%3CT,+Error%3E"
class="anchor">§</a>

### impl\<T: <a href="trait.MacroResult.html" class="trait"
title="trait synstructure::MacroResult">MacroResult</a>\> <a href="trait.MacroResult.html" class="trait"
title="trait synstructure::MacroResult">MacroResult</a> for <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<T\>

</div>

<div class="impl-items">

<div id="method.into_result-2" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#2514-2519"
class="src rightside">Source</a><a href="#method.into_result-2" class="anchor">§</a>

#### fn <a href="#tymethod.into_result" class="fn">into_result</a>(self) -\> <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
