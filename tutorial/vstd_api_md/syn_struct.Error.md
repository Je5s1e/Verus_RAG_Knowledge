<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Struct <span class="struct">Error</span> Copy item path

<span class="sub-heading"><a href="../src/syn/error.rs.html#105-107" class="src">Source</a>
</span>

</div>

``` rust
pub struct Error { /* private fields */ }
```

Expand description

<div class="docblock">

Error returned when a Syn parser cannot parse the input tokens.

## <a href="#error-reporting-in-proc-macros" class="doc-anchor">§</a>Error reporting in proc macros

The correct way to report errors back to the compiler from a procedural
macro is by emitting an appropriately spanned invocation of
[`compile_error!`](https://doc.rust-lang.org/1.92.0/core/macro.compile_error.html "macro core::compile_error")
in the generated code. This produces a better diagnostic message than
simply panicking the macro.

When parsing macro input, the
[`parse_macro_input!`](macro.parse_macro_input.html "macro syn::parse_macro_input")
macro handles the conversion to `compile_error!` automatically.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::parse::{Parse, ParseStream, Result};
use syn::{parse_macro_input, ItemFn};

#[proc_macro_attribute]
pub fn my_attr(args: TokenStream, input: TokenStream) -> TokenStream {
    let args = parse_macro_input!(args as MyAttrArgs);
    let input = parse_macro_input!(input as ItemFn);

    /* ... */
}

struct MyAttrArgs {
    ...
}

impl Parse for MyAttrArgs {
    fn parse(input: ParseStream) -> Result<Self> {
        ...
    }
}
```

</div>

For errors that arise later than the initial parsing stage, the
[`.to_compile_error()`](struct.Error.html#method.to_compile_error "method syn::Error::to_compile_error")
or
[`.into_compile_error()`](struct.Error.html#method.into_compile_error "method syn::Error::into_compile_error")
methods can be used to perform an explicit conversion to
`compile_error!`.

<div class="example-wrap">

``` rust
#[proc_macro_derive(MyDerive)]
pub fn my_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);

    // fn(DeriveInput) -> syn::Result<proc_macro2::TokenStream>
    expand::my_derive(input)
        .unwrap_or_else(syn::Error::into_compile_error)
        .into()
}
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Error" class="section impl">

<a href="../src/syn/error.rs.html#132-279"
class="src rightside">Source</a><a href="#impl-Error" class="anchor">§</a>

### impl <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../src/syn/error.rs.html#163-177"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>\<T: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a>\>(span: <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>, message: T) -\> Self

</div>

<div class="docblock">

Usually the
[`ParseStream::error`](parse/struct.ParseBuffer.html#method.error "method syn::parse::ParseBuffer::error")
method will be used instead, which automatically uses the correct span
from the current position of the parse stream.

Use `Error::new` when the error needs to be triggered on some span other
than where the parse stream is currently positioned.

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{Error, Ident, LitStr, Result, Token};
use syn::parse::ParseStream;

// Parses input that looks like `name = "string"` where the key must be
// the identifier `name` and the value may be any string literal.
// Returns the string literal.
fn parse_name(input: ParseStream) -> Result<LitStr> {
    let name_token: Ident = input.parse()?;
    if name_token != "name" {
        // Trigger an error not on the current position of the stream,
        // but on the position of the unexpected identifier.
        return Err(Error::new(name_token.span(), "expected `name`"));
    }
    input.parse::<Token![=]>()?;
    let s: LitStr = input.parse()?;
    Ok(s)
}
```

</div>

</div>

<div id="method.new_spanned" class="section method">

<a href="../src/syn/error.rs.html#194-208"
class="src rightside">Source</a>

#### pub fn <a href="#method.new_spanned" class="fn">new_spanned</a>\<T: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, U: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a>\>(tokens: T, message: U) -\> Self

</div>

<div class="docblock">

Creates an error with the specified message spanning the given syntax
tree node.

Unlike the `Error::new` constructor, this constructor takes an argument
`tokens` which is a syntax tree node. This allows the resulting `Error`
to attempt to span all tokens inside of `tokens`. While you would
typically be able to use the `Spanned` trait with the above `Error::new`
constructor, implementation limitations today mean that
`Error::new_spanned` may provide a higher-quality error message on
stable Rust.

When in doubt it’s recommended to stick to `Error::new` (or
`ParseStream::error`)!

</div>

<div id="method.span" class="section method">

<a href="../src/syn/error.rs.html#215-221"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

The source location of the error.

Spans are not thread-safe so this function returns `Span::call_site()`
if called from a different thread than the one on which the `Error` was
originally created.

</div>

<div id="method.to_compile_error" class="section method">

<a href="../src/syn/error.rs.html#230-236"
class="src rightside">Source</a>

#### pub fn <a href="#method.to_compile_error" class="fn">to_compile_error</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Render the error as an invocation of
[`compile_error!`](https://doc.rust-lang.org/1.92.0/core/macro.compile_error.html "macro core::compile_error").

The
[`parse_macro_input!`](macro.parse_macro_input.html "macro syn::parse_macro_input")
macro provides a convenient way to invoke this method correctly in a
procedural macro.

</div>

<div id="method.into_compile_error" class="section method">

<a href="../src/syn/error.rs.html#270-272"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_compile_error" class="fn">into_compile_error</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Render the error as an invocation of
[`compile_error!`](https://doc.rust-lang.org/1.92.0/core/macro.compile_error.html "macro core::compile_error").

##### <a href="#example-1" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::{parse_macro_input, DeriveInput, Error};

#[proc_macro_derive(MyTrait)]
pub fn derive_my_trait(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    my_trait::expand(input)
        .unwrap_or_else(Error::into_compile_error)
        .into()
}

mod my_trait {
    use proc_macro2::TokenStream;
    use syn::{DeriveInput, Result};

    pub(crate) fn expand(input: DeriveInput) -> Result<TokenStream> {
        /* ... */
    }
}
```

</div>

</div>

<div id="method.combine" class="section method">

<a href="../src/syn/error.rs.html#276-278"
class="src rightside">Source</a>

#### pub fn <a href="#method.combine" class="fn">combine</a>(&mut self, another: <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>)

</div>

<div class="docblock">

Add another error message to self such that when `to_compile_error()` is
called, both errors will be emitted together.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#383-389"
class="src rightside">Source</a><a href="#impl-Clone-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/syn/error.rs.html#384-388"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

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

<div id="impl-Debug-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#355-369"
class="src rightside">Source</a><a href="#impl-Debug-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/syn/error.rs.html#356-368"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, formatter: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Display-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#377-381"
class="src rightside">Source</a><a href="#impl-Display-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../src/syn/error.rs.html#378-380"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt"
class="fn">fmt</a>(&self, formatter: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt)

</div>

</div>

<div id="impl-Error-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#409" class="src rightside">Source</a><a href="#impl-Error-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html"
class="trait" title="trait core::error::Error">Error</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.source" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.30.0">1.30.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/error.rs.html#111"
class="src">Source</a></span><a href="#method.source" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.source"
class="fn">source</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<&(dyn <a href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html"
class="trait" title="trait core::error::Error">Error</a> + 'static)\>

</div>

<div class="docblock">

Returns the lower-level source of this error, if any. [Read
more](https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.source)

</div>

<div id="method.description" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/error.rs.html#137"
class="src">Source</a></span><a href="#method.description" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.description"
class="fn">description</a>(&self) -\> &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<span class="item-info"></span>

<div class="stab deprecated">

👎Deprecated since 1.42.0: use the Display impl or to_string()

</div>

<div class="docblock">

[Read
more](https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.description)

</div>

<div id="method.cause" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/error.rs.html#147"
class="src">Source</a></span><a href="#method.cause" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.cause"
class="fn">cause</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<&dyn <a href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html"
class="trait" title="trait core::error::Error">Error</a>\>

</div>

<span class="item-info"></span>

<div class="stab deprecated">

👎Deprecated since 1.33.0: replaced by Error::source, which can support
downcasting

</div>

<div id="method.provide" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/error.rs.html#210"
class="src rightside">Source</a><a href="#method.provide" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.provide"
class="fn">provide</a>\<'a\>(&'a self, request: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/error/struct.Request.html"
class="struct" title="struct core::error::Request">Request</a>\<'a\>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API.
(`error_generic_member_access`)

</div>

<div class="docblock">

Provides type-based access to context intended for error reports. [Read
more](https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html#method.provide)

</div>

</div>

<div id="impl-Extend%3CError%3E-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#467-473"
class="src rightside">Source</a><a href="#impl-Extend%3CError%3E-for-Error" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>\> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../src/syn/error.rs.html#468-472"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<T: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>\>\>(&mut self, iter: T)

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

<div id="impl-From%3CLexError%3E-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#411-415"
class="src rightside">Source</a><a href="#impl-From%3CLexError%3E-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="../proc_macro2/struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>\> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/syn/error.rs.html#412-414"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(err: <a href="../proc_macro2/struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-IntoIterator-for-%26Error" class="section impl">

<a href="../src/syn/error.rs.html#442-451"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26Error" class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../src/syn/error.rs.html#443" class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-1"
class="section associatedtype trait-impl">

<a href="../src/syn/error.rs.html#444" class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = Iter\<'a\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../src/syn/error.rs.html#446-450"
class="src rightside">Source</a><a href="#method.into_iter-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-IntoIterator-for-Error" class="section impl">

<a href="../src/syn/error.rs.html#417-426"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-Error" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../src/syn/error.rs.html#418" class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../src/syn/error.rs.html#419" class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = IntoIter

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../src/syn/error.rs.html#421-425"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Error" class="section impl">

<a href="#impl-Freeze-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div id="impl-RefUnwindSafe-for-Error" class="section impl">

<a href="#impl-RefUnwindSafe-for-Error" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div id="impl-Send-for-Error" class="section impl">

<a href="#impl-Send-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div id="impl-Sync-for-Error" class="section impl">

<a href="#impl-Sync-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div id="impl-Unpin-for-Error" class="section impl">

<a href="#impl-Unpin-for-Error" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div id="impl-UnwindSafe-for-Error" class="section impl">

<a href="#impl-UnwindSafe-for-Error" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

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

<div id="method.from-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

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
