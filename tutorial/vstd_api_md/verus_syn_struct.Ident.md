<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Struct <span class="struct">Ident</span> Copy item path

<span class="sub-heading"><a href="../src/proc_macro2/lib.rs.html#968" class="src">Source</a>
</span>

</div>

``` rust
pub struct Ident { /* private fields */ }
```

Expand description

<div class="docblock">

A word of Rust code, which may be a keyword or legal variable name.

An identifier consists of at least one Unicode code point, the first of
which has the XID_Start property and the rest of which have the
XID_Continue property.

- The empty string is not an identifier. Use `Option<Ident>`.
- A lifetime is not an identifier. Use `syn::Lifetime` instead.

An identifier constructed with `Ident::new` is permitted to be a Rust
keyword, though parsing one through its
[`Parse`](https://docs.rs/syn/2.0/syn/parse/trait.Parse.html)
implementation rejects Rust keywords. Use `input.call(Ident::parse_any)`
when parsing to match the behaviour of `Ident::new`.

## <a href="#examples" class="doc-anchor">§</a>Examples

A new ident can be created from a string using the `Ident::new`
function. A span must be provided explicitly which governs the name
resolution behavior of the resulting identifier.

<div class="example-wrap">

``` rust
use proc_macro2::{Ident, Span};

fn main() {
    let call_ident = Ident::new("calligraphy", Span::call_site());

    println!("{}", call_ident);
}
```

</div>

An ident can be interpolated into a token stream using the `quote!`
macro.

<div class="example-wrap">

``` rust
use proc_macro2::{Ident, Span};
use quote::quote;

fn main() {
    let ident = Ident::new("demo", Span::call_site());

    // Create a variable binding whose name is this ident.
    let expanded = quote! { let #ident = 10; };

    // Create a variable binding with a slightly different name.
    let temp_ident = Ident::new(&format!("new_{}", ident), Span::call_site());
    let expanded = quote! { let #temp_ident = 10; };
}
```

</div>

A string representation of the ident is available through the
`to_string()` method.

<div class="example-wrap">

``` rust
// Examine the ident as a string.
let ident_string = ident.to_string();
if ident_string.len() > 60 {
    println!("Very long identifier: {}", ident_string)
}
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#973"
class="src rightside">Source</a><a href="#impl-Ident" class="anchor">§</a>

### impl <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1020"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>(string: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>, span: <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Creates a new `Ident` with the given `string` as well as the specified
`span`.

The `string` argument must be a valid identifier permitted by the
language, otherwise the function will panic.

Note that `span`, currently in rustc, configures the hygiene information
for this identifier.

As of this time `Span::call_site()` explicitly opts-in to “call-site”
hygiene meaning that identifiers created with this span will be resolved
as if they were written directly at the location of the macro call, and
other code at the macro call site will be able to refer to them as well.

Later spans like `Span::def_site()` will allow to opt-in to
“definition-site” hygiene meaning that identifiers created with this
span will be resolved at the location of the macro definition and other
code at the macro call site will not be able to refer to them.

Due to the current importance of hygiene this constructor, unlike other
tokens, requires a `Span` to be specified at construction.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the input string is neither a keyword nor a legal variable
name. If you are not sure whether the string contains an identifier and
need to handle an error case, use
[`syn::parse_str`](https://docs.rs/syn/2.0/syn/fn.parse_str.html)`::<Ident>`
rather than `Ident::new`.

</div>

<div id="method.new_raw" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1030"
class="src rightside">Source</a>

#### pub fn <a href="#method.new_raw" class="fn">new_raw</a>(string: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>, span: <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Same as `Ident::new`, but creates a raw identifier (`r#ident`). The
`string` argument must be a valid identifier permitted by the language
(including keywords, e.g. `fn`). Keywords which are usable in path
segments (e.g. `self`, `super`) are not supported, and will cause a
panic.

</div>

<div id="method.span" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1035"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns the span of this `Ident`.

</div>

<div id="method.set_span" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1041"
class="src rightside">Source</a>

#### pub fn <a href="#method.set_span" class="fn">set_span</a>(&mut self, span: <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div class="docblock">

Configures the span of this `Ident`, possibly changing its hygiene
context.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#967"
class="src rightside">Source</a><a href="#impl-Clone-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#967"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1089"
class="src rightside">Source</a><a href="#impl-Debug-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1090"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>, <a href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Error.html"
class="struct" title="struct core::fmt::Error">Error</a>\>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Display-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1083"
class="src rightside">Source</a><a href="#impl-Display-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

<div class="docblock">

Prints the identifier as a string that should be losslessly convertible
back into the same identifier.

</div>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1084"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>, <a href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Error.html"
class="struct" title="struct core::fmt::Error">Error</a>\>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt)

</div>

</div>

<div id="impl-Extend%3CIdent%3E-for-TokenStream" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#319"
class="src rightside">Source</a><a href="#impl-Extend%3CIdent%3E-for-TokenStream" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>\> for <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#320"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I\>(&mut self, tokens: I)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item
= <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>\>,

</div>

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

</div>

<div id="method.extend_one" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_one"
class="fn">extend_one</a>(&mut self, item: A)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Extends a collection with exactly one element.

</div>

<div id="method.extend_reserve" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve"
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Reserves capacity in a collection for the given number of additional
elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve)

</div>

</div>

<div id="impl-From%3CCrate%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#28"
class="src rightside">Source</a><a href="#impl-From%3CCrate%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.Crate.html" class="struct"
title="struct verus_syn::token::Crate">Crate</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-5" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#28"
class="src rightside">Source</a><a href="#method.from-5" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.Crate.html" class="struct"
title="struct verus_syn::token::Crate">Crate</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CExtern%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#29"
class="src rightside">Source</a><a href="#impl-From%3CExtern%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.Extern.html" class="struct"
title="struct verus_syn::token::Extern">Extern</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-6" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#29"
class="src rightside">Source</a><a href="#method.from-6" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.Extern.html" class="struct"
title="struct verus_syn::token::Extern">Extern</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CIdent%3E-for-Member" class="section impl">

<a href="../src/verus_syn/expr.rs.html#1035-1039"
class="src rightside">Source</a><a href="#impl-From%3CIdent%3E-for-Member" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>\> for <a href="enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/verus_syn/expr.rs.html#1036-1038"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(ident: <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>) -\> <a href="enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CIdent%3E-for-TypeParam" class="section impl">

<a href="../src/verus_syn/generics.rs.html#385-396"
class="src rightside">Source</a><a href="#impl-From%3CIdent%3E-for-TypeParam" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>\> for <a href="struct.TypeParam.html" class="struct"
title="struct verus_syn::TypeParam">TypeParam</a>

</div>

<div class="impl-items">

<div id="method.from-1" class="section method trait-impl">

<a href="../src/verus_syn/generics.rs.html#386-395"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(ident: <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CSelfType%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#26"
class="src rightside">Source</a><a href="#impl-From%3CSelfType%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.SelfType.html" class="struct"
title="struct verus_syn::token::SelfType">SelfType</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-3" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#26"
class="src rightside">Source</a><a href="#method.from-3" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.SelfType.html" class="struct"
title="struct verus_syn::token::SelfType">SelfType</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CSelfValue%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#25"
class="src rightside">Source</a><a href="#impl-From%3CSelfValue%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.SelfValue.html" class="struct"
title="struct verus_syn::token::SelfValue">SelfValue</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-2" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#25"
class="src rightside">Source</a><a href="#method.from-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.SelfValue.html" class="struct"
title="struct verus_syn::token::SelfValue">SelfValue</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CSuper%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#27"
class="src rightside">Source</a><a href="#impl-From%3CSuper%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.Super.html" class="struct"
title="struct verus_syn::token::Super">Super</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-4" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#27"
class="src rightside">Source</a><a href="#method.from-4" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.Super.html" class="struct"
title="struct verus_syn::token::Super">Super</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-From%3CUnderscore%3E-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#31-35"
class="src rightside">Source</a><a href="#impl-From%3CUnderscore%3E-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="token/struct.Underscore.html" class="struct"
title="struct verus_syn::token::Underscore">Underscore</a>\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.from-7" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#32-34"
class="src rightside">Source</a><a href="#method.from-7" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(token: <a href="token/struct.Underscore.html" class="struct"
title="struct verus_syn::token::Underscore">Underscore</a>) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-Hash-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1075"
class="src rightside">Source</a><a href="#impl-Hash-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1076"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<H\>(&self, hasher: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>,

</div>

</div>

<div class="docblock">

Feeds this value into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash)

</div>

<div id="method.hash_slice" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.3.0">1.3.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/hash/mod.rs.html#235-237"
class="src">Source</a></span><a href="#method.hash_slice" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice"
class="fn">hash_slice</a>\<H\>(data: &\[Self\], state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Feeds a slice of this type into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice)

</div>

</div>

<div id="impl-IdentExt-for-Ident" class="section impl">

<a href="../src/verus_syn/ext.rs.html#97-114"
class="src rightside">Source</a><a href="#impl-IdentExt-for-Ident" class="anchor">§</a>

### impl <a href="ext/trait.IdentExt.html" class="trait"
title="trait verus_syn::ext::IdentExt">IdentExt</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.parse_any" class="section method trait-impl">

<a href="../src/verus_syn/ext.rs.html#99-104"
class="src rightside">Source</a><a href="#method.parse_any" class="anchor">§</a>

#### fn <a href="ext/trait.IdentExt.html#tymethod.parse_any"
class="fn">parse_any</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Parses any identifier including keywords. [Read
more](ext/trait.IdentExt.html#tymethod.parse_any)

</div>

<div id="method.unraw" class="section method trait-impl">

<a href="../src/verus_syn/ext.rs.html#106-113"
class="src rightside">Source</a><a href="#method.unraw" class="anchor">§</a>

#### fn <a href="ext/trait.IdentExt.html#tymethod.unraw" class="fn">unraw</a>(&self) -\> <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Strips the raw marker `r#`, if any, from the beginning of an ident.
[Read more](ext/trait.IdentExt.html#tymethod.unraw)

</div>

<div id="associatedconstant.peek_any"
class="section associatedconstant trait-impl">

<a href="../src/verus_syn/ext.rs.html#65"
class="src rightside">Source</a><a href="#associatedconstant.peek_any" class="anchor">§</a>

#### const <a href="ext/trait.IdentExt.html#associatedconstant.peek_any"
class="constant">peek_any</a>: PeekFn = private::PeekFn

</div>

<div class="docblock">

Peeks any identifier including keywords. Usage:
`input.peek(Ident::peek_any)` [Read
more](ext/trait.IdentExt.html#associatedconstant.peek_any)

</div>

</div>

<div id="impl-IdentFragment-for-Ident" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#46"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-Ident" class="anchor">§</a>

### impl <a href="../quote/ident_fragment/trait.IdentFragment.html" class="trait"
title="trait quote::ident_fragment::IdentFragment">IdentFragment</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.span-1" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#47"
class="src rightside">Source</a><a href="#method.span-1" class="anchor">§</a>

#### fn <a href="../quote/ident_fragment/trait.IdentFragment.html#method.span"
class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div class="docblock">

Span associated with this `IdentFragment`. [Read
more](../quote/ident_fragment/trait.IdentFragment.html#method.span)

</div>

<div id="method.fmt-2" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#51"
class="src rightside">Source</a><a href="#method.fmt-2" class="anchor">§</a>

#### fn <a href="../quote/ident_fragment/trait.IdentFragment.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>, <a href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Error.html"
class="struct" title="struct core::fmt::Error">Error</a>\>

</div>

<div class="docblock">

Format this value as an identifier fragment.

</div>

</div>

<div id="impl-Ord-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1069"
class="src rightside">Source</a><a href="#impl-Ord-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.cmp" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1070"
class="src rightside">Source</a><a href="#method.cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#tymethod.cmp"
class="fn">cmp</a>(&self, other: &<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>

</div>

<div class="docblock">

This method returns an
[`Ordering`](https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html "enum core::cmp::Ordering")
between `self` and `other`. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#tymethod.cmp)

</div>

<div id="method.max" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.21.0">1.21.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1021-1023"
class="src">Source</a></span><a href="#method.max" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.max"
class="fn">max</a>(self, other: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Compares and returns the maximum of two values. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.max)

</div>

<div id="method.min" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.21.0">1.21.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1060-1062"
class="src">Source</a></span><a href="#method.min" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.min"
class="fn">min</a>(self, other: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Compares and returns the minimum of two values. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.min)

</div>

<div id="method.clamp" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.50.0">1.50.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1086-1088"
class="src">Source</a></span><a href="#method.clamp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.clamp"
class="fn">clamp</a>(self, min: Self, max: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Restrict a value to a certain interval. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.clamp)

</div>

</div>

<div id="impl-Parse-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#76-93"
class="src rightside">Source</a><a href="#impl-Parse-for-Ident" class="anchor">§</a>

### impl <a href="parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.parse" class="section method trait-impl">

<a href="../src/verus_syn/ident.rs.html#77-92"
class="src rightside">Source</a><a href="#method.parse" class="anchor">§</a>

#### fn <a href="parse/trait.Parse.html#tymethod.parse" class="fn">parse</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-PartialEq%3CT%3E-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1052-1054"
class="src rightside">Source</a><a href="#impl-PartialEq%3CT%3E-for-Ident" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<T\> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.AsRef.html"
class="trait" title="trait core::convert::AsRef">AsRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.eq-1" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1056"
class="src rightside">Source</a><a href="#method.eq-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne-1" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-PartialEq-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1046"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1047"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-PartialOrd-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1063"
class="src rightside">Source</a><a href="#impl-PartialOrd-for-Ident" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.partial_cmp" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1064"
class="src rightside">Source</a><a href="#method.partial_cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp"
class="fn">partial_cmp</a>(&self, other: &<a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>

</div>

<div class="docblock">

This method returns an ordering between `self` and `other` values if one
exists. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

</div>

<div id="method.lt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1398"
class="src">Source</a></span><a href="#method.lt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt"
class="fn">lt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than (for `self` and `other`) and is used by the `<`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt)

</div>

<div id="method.le" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1416"
class="src">Source</a></span><a href="#method.le" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le"
class="fn">le</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than or equal to (for `self` and `other`) and is used by the
`<=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le)

</div>

<div id="method.gt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1434"
class="src">Source</a></span><a href="#method.gt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt"
class="fn">gt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than (for `self` and `other`) and is used by the `>`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt)

</div>

<div id="method.ge" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1452"
class="src">Source</a></span><a href="#method.ge" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge"
class="fn">ge</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than or equal to (for `self` and `other`) and is used by
the `>=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge)

</div>

</div>

<div id="impl-ToTokens-for-Ident" class="section impl">

<a href="../src/quote/to_tokens.rs.html#242"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Ident" class="anchor">§</a>

### impl <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#243"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Eq-for-Ident" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1061"
class="src rightside">Source</a><a href="#impl-Eq-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Token-for-Ident" class="section impl">

<a href="../src/verus_syn/ident.rs.html#95-107"
class="src rightside">Source</a><a href="#impl-Token-for-Ident" class="anchor">§</a>

### impl <a href="token/trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Ident" class="section impl">

<a href="#impl-Freeze-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-RefUnwindSafe-for-Ident" class="section impl">

<a href="#impl-RefUnwindSafe-for-Ident" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Send-for-Ident" class="section impl">

<a href="#impl-Send-for-Ident" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Sync-for-Ident" class="section impl">

<a href="#impl-Sync-for-Ident" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-Unpin-for-Ident" class="section impl">

<a href="#impl-Unpin-for-Ident" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div id="impl-UnwindSafe-for-Ident" class="section impl">

<a href="#impl-UnwindSafe-for-Ident" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from-8" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-8" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-Spanned-for-T" class="section impl">

<a href="../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="spanned/trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span-2" class="section method trait-impl">

<a href="../src/verus_syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span-2" class="anchor">§</a>

#### fn <a href="spanned/trait.Spanned.html#tymethod.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
if this node is empty.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-ToString-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2866"
class="src rightside">Source</a><a href="#impl-ToString-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html"
class="trait" title="trait alloc::string::ToString">ToString</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.to_string" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2868"
class="src rightside">Source</a><a href="#method.to_string" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string"
class="fn">to_string</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="docblock">

Converts the given value to a `String`. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
