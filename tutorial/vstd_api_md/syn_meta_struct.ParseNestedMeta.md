<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[meta](index.html)

</div>

# Struct <span class="struct">ParseNestedMeta</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/meta.rs.html#164-167" class="src">Source</a>
</span>

</div>

``` rust
#[non_exhaustive]pub struct ParseNestedMeta<'a> {
    pub path: Path,
    pub input: ParseStream<'a>,
}
```

Expand description

<div class="docblock">

Context for parsing a single property in the conventional syntax for
structured attributes.

## <a href="#examples" class="doc-anchor">§</a>Examples

Refer to usage examples on the following two entry-points:

- [`Attribute::parse_nested_meta`](../struct.Attribute.html#method.parse_nested_meta "method syn::Attribute::parse_nested_meta")
  if you have an entire `Attribute` to parse. Always use this if
  possible. Generally this is able to produce better error messages
  because `Attribute` holds span information for all of the delimiters
  therein.

- [`syn::meta::parser`](fn.parser.html "fn syn::meta::parser") if you
  are implementing a `proc_macro_attribute` macro and parsing the
  arguments to the attribute macro, i.e. the ones written in the same
  attribute that dispatched the macro invocation. Rustc does not pass
  span information for the surrounding delimiters into the attribute
  macro invocation in this situation, so error messages might be less
  precise.

</div>

## Fields (Non-exhaustive)<a href="#fields" class="anchor">§</a>

This struct is marked as non-exhaustive

<div class="docblock">

Non-exhaustive structs could have additional fields added in future.
Therefore, non-exhaustive structs cannot be constructed in external
crates using the traditional `Struct { .. }` syntax; cannot be matched
against without a wildcard `..`; and struct update syntax will not work.

</div>

<span id="structfield.path"
class="structfield section-header"><a href="#structfield.path" class="anchor field">§</a>`path: `<a href="../struct.Path.html" class="struct"
title="struct syn::Path"><code>Path</code></a></span><span id="structfield.input"
class="structfield section-header"><a href="#structfield.input" class="anchor field">§</a>`input: `<a href="../parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream"><code>ParseStream</code></a>`<'a>`</span>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-ParseNestedMeta%3C'a%3E" class="section impl">

<a href="../../src/syn/meta.rs.html#169-383"
class="src rightside">Source</a><a href="#impl-ParseNestedMeta%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.value" class="section method">

<a href="../../src/syn/meta.rs.html#202-205"
class="src rightside">Source</a>

#### pub fn <a href="#method.value" class="fn">value</a>(&self) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="../parse/type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'a\>\>

</div>

<div class="docblock">

Used when parsing `key = "value"` syntax.

All it does is advance `meta.input` past the `=` sign in the input. You
could accomplish the same effect by writing
`meta.parse::<Token![=]>()?`, so at most it is a minor convenience to
use `meta.value()?`.

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parse_quote, Attribute, LitStr};

let attr: Attribute = parse_quote! {
    #[tea(kind = "EarlGrey")]
};
                                         // conceptually:
if attr.path().is_ident("tea") {         // this parses the `tea`
    attr.parse_nested_meta(|meta| {      // this parses the `(`
        if meta.path.is_ident("kind") {  // this parses the `kind`
            let value = meta.value()?;   // this parses the `=`
            let s: LitStr = value.parse()?;  // this parses `"EarlGrey"`
            if s.value() == "EarlGrey" {
                // ...
            }
            Ok(())
        } else {
            Err(meta.error("unsupported attribute"))
        }
    })?;
}
```

</div>

</div>

<div id="method.parse_nested_meta" class="section method">

<a href="../../src/syn/meta.rs.html#271-278"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_nested_meta" class="fn">parse_nested_meta</a>( &self, logic: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\>, ) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\>

</div>

<div class="docblock">

Used when parsing `list(...)` syntax **if** the content inside the
nested parentheses is also expected to conform to Rust’s structured
attribute convention.

##### <a href="#example-1" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parse_quote, Attribute};

let attr: Attribute = parse_quote! {
    #[tea(with(sugar, milk))]
};

if attr.path().is_ident("tea") {
    attr.parse_nested_meta(|meta| {
        if meta.path.is_ident("with") {
            meta.parse_nested_meta(|meta| {  // <---
                if meta.path.is_ident("sugar") {
                    // Here we can go even deeper if needed.
                    Ok(())
                } else if meta.path.is_ident("milk") {
                    Ok(())
                } else {
                    Err(meta.error("unsupported ingredient"))
                }
            })
        } else {
            Err(meta.error("unsupported tea property"))
        }
    })?;
}
```

</div>

##### <a href="#counterexample" class="doc-anchor">§</a>Counterexample

If you don’t need `parse_nested_meta`’s help in parsing the content
written within the nested parentheses, keep in mind that you can always
just parse it yourself from the exposed ParseStream. Rust syntax permits
arbitrary tokens within those parentheses so for the crazier stuff,
`parse_nested_meta` is not what you want.

<div class="example-wrap">

``` rust
use syn::{parenthesized, parse_quote, Attribute, LitInt};

let attr: Attribute = parse_quote! {
    #[repr(align(32))]
};

let mut align: Option<LitInt> = None;
if attr.path().is_ident("repr") {
    attr.parse_nested_meta(|meta| {
        if meta.path.is_ident("align") {
            let content;
            parenthesized!(content in meta.input);
            align = Some(content.parse()?);
            Ok(())
        } else {
            Err(meta.error("unsupported repr"))
        }
    })?;
}
```

</div>

</div>

<div id="method.error" class="section method">

<a href="../../src/syn/meta.rs.html#378-382"
class="src rightside">Source</a>

#### pub fn <a href="#method.error" class="fn">error</a>(&self, msg: impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a>) -\> <a href="../struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="docblock">

Report that the attribute’s content did not conform to expectations.

The span of the resulting error will cover `meta.path` *and* everything
that has been parsed so far since it.

There are 2 ways you might call this. First, if `meta.path` is not
something you recognize:

<div class="example-wrap">

``` rust
attr.parse_nested_meta(|meta| {
    if meta.path.is_ident("kind") {
        // ...
        Ok(())
    } else {
        Err(meta.error("unsupported tea property"))
    }
})?;
```

</div>

In this case, it behaves exactly like
`syn::Error::new_spanned(&meta.path, "message...")`.

<div class="example-wrap">

``` console
error: unsupported tea property
 --> src/main.rs:3:26
  |
3 | #[tea(kind = "EarlGrey", wat = "foo")]
  |                          ^^^
```

</div>

More usefully, the second place is if you’ve already parsed a value but
have decided not to accept the value:

<div class="example-wrap">

``` rust
use syn::Expr;

attr.parse_nested_meta(|meta| {
    if meta.path.is_ident("kind") {
        let expr: Expr = meta.value()?.parse()?;
        match expr {
            Expr::Lit(expr) => /* ... */
            Expr::Path(expr) => /* ... */
            Expr::Macro(expr) => /* ... */
            _ => Err(meta.error("tea kind must be a string literal, path, or macro")),
        }
    } else /* as above */

})?;
```

</div>

<div class="example-wrap">

``` console
error: tea kind must be a string literal, path, or macro
 --> src/main.rs:3:7
  |
3 | #[tea(kind = async { replicator.await })]
  |       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

</div>

Often you may want to use `syn::Error::new_spanned` even in this
situation. In the above code, that would be:

<div class="example-wrap">

``` rust
    match expr {
        Expr::Lit(expr) => /* ... */
        Expr::Path(expr) => /* ... */
        Expr::Macro(expr) => /* ... */
        _ => Err(Error::new_spanned(expr, "unsupported expression type for `kind`")),
    }
```

</div>

<div class="example-wrap">

``` console
error: unsupported expression type for `kind`
 --> src/main.rs:3:14
  |
3 | #[tea(kind = async { replicator.await })]
  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^
```

</div>

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-ParseNestedMeta%3C'a%3E" class="section impl">

<a href="#impl-Freeze-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div id="impl-RefUnwindSafe-for-ParseNestedMeta%3C'a%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div id="impl-Send-for-ParseNestedMeta%3C'a%3E" class="section impl">

<a href="#impl-Send-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div id="impl-Sync-for-ParseNestedMeta%3C'a%3E" class="section impl">

<a href="#impl-Sync-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div id="impl-Unpin-for-ParseNestedMeta%3C'a%3E" class="section impl">

<a href="#impl-Unpin-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

</div>

<div id="impl-UnwindSafe-for-ParseNestedMeta%3C'a%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-ParseNestedMeta%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.ParseNestedMeta.html" class="struct"
title="struct syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'a\>

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
