<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[proc_macro2](index.html)

</div>

# Struct <span class="struct">LexError</span> Copy item path

<span class="sub-heading"><a href="../src/proc_macro2/lib.rs.html#217-220" class="src">Source</a>
</span>

</div>

``` rust
pub struct LexError { /* private fields */ }
```

Expand description

<div class="docblock">

Error returned from `TokenStream::from_str`.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-LexError" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#368-372"
class="src rightside">Source</a><a href="#impl-LexError" class="anchor">§</a>

### impl <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div class="impl-items">

<div id="method.span" class="section method">

<a href="../src/proc_macro2/lib.rs.html#369-371"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-LexError" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#374-378"
class="src rightside">Source</a><a href="#impl-Debug-for-LexError" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#375-377"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Display-for-LexError" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#380-384"
class="src rightside">Source</a><a href="#impl-Display-for-LexError" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#381-383"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt)

</div>

</div>

<div id="impl-Error-for-LexError" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#386"
class="src rightside">Source</a><a href="#impl-Error-for-LexError" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/error/trait.Error.html"
class="trait" title="trait core::error::Error">Error</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

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

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-LexError" class="section impl">

<a href="#impl-Freeze-for-LexError" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div id="impl-RefUnwindSafe-for-LexError" class="section impl">

<a href="#impl-RefUnwindSafe-for-LexError" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div id="impl-Send-for-LexError" class="section impl">

<a href="#impl-Send-for-LexError" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div id="impl-Sync-for-LexError" class="section impl">

<a href="#impl-Sync-for-LexError" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div id="impl-Unpin-for-LexError" class="section impl">

<a href="#impl-Unpin-for-LexError" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div id="impl-UnwindSafe-for-LexError" class="section impl">

<a href="#impl-UnwindSafe-for-LexError" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

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

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

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
