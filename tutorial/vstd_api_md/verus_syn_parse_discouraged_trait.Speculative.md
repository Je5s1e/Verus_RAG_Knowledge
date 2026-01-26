<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../../index.html)::[parse](../index.html)::[discouraged](index.html)

</div>

# Trait <span class="trait">Speculative</span> Copy item path

<span class="sub-heading"><a href="../../../src/verus_syn/discouraged.rs.html#13-165"
class="src">Source</a> </span>

</div>

``` rust
pub trait Speculative {
    // Required method
    fn advance_to(&self, fork: &Self);
}
```

Expand description

<div class="docblock">

Extensions to the `ParseStream` API to support speculative parsing.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.advance_to" class="section method">

<a href="../../../src/verus_syn/discouraged.rs.html#164"
class="src rightside">Source</a>

#### fn <a href="#tymethod.advance_to" class="fn">advance_to</a>(&self, fork: &Self)

</div>

<div class="docblock">

Advance this parse stream to the position of a forked parse stream.

This is the opposite operation to
[`ParseStream::fork`](../struct.ParseBuffer.html#method.fork "method verus_syn::parse::ParseBuffer::fork").
You can fork a parse stream, perform some speculative parsing, then join
the original stream to the fork to “commit” the parsing from the fork to
the main stream.

If you can avoid doing this, you should, as it limits the ability to
generate useful errors. That said, it is often the only way to parse
syntax of the form `A* B*` for arbitrary syntax `A` and `B`. The problem
is that when the fork fails to parse an `A`, it’s impossible to tell
whether that was because of a syntax error and the user meant to provide
an `A`, or that the `A`s are finished and it’s time to start parsing
`B`s. Use with care.

Also note that if `A` is a subset of `B`, `A* B*` can be parsed by
parsing `B*` and removing the leading members of `A` from the
repetition, bypassing the need to involve the downsides associated with
speculative parsing.

##### <a href="#example" class="doc-anchor">§</a>Example

There has been chatter about the possibility of making the colons in the
turbofish syntax like `path::to::<T>` no longer required by accepting
`path::to<T>` in expression position. Specifically, according to [RFC
2544](https://github.com/rust-lang/rfcs/pull/2544),
[`PathSegment`](../../struct.PathSegment.html "struct verus_syn::PathSegment")
parsing should always try to consume a following `<` token as the start
of generic arguments, and reset to the `<` if that fails (e.g. the token
is acting as a less-than operator).

This is the exact kind of parsing behavior which requires the “fork,
try, commit” behavior that
[`ParseStream::fork`](../struct.ParseBuffer.html#method.fork "method verus_syn::parse::ParseBuffer::fork")
discourages. With `advance_to`, we can avoid having to parse the
speculatively parsed content a second time.

This change in behavior can be implemented in syn by replacing just the
`Parse` implementation for `PathSegment`:

<div class="example-wrap">

``` rust
use syn::parse::discouraged::Speculative;

pub struct PathSegment {
    pub ident: Ident,
    pub arguments: PathArguments,
}

impl Parse for PathSegment {
    fn parse(input: ParseStream) -> Result<Self> {
        if input.peek(Token![super])
            || input.peek(Token![self])
            || input.peek(Token![Self])
            || input.peek(Token![crate])
        {
            let ident = input.call(Ident::parse_any)?;
            return Ok(PathSegment::from(ident));
        }

        let ident = input.parse()?;
        if input.peek(Token![::]) && input.peek3(Token![<]) {
            return Ok(PathSegment {
                ident,
                arguments: PathArguments::AngleBracketed(input.parse()?),
            });
        }
        if input.peek(Token![<]) && !input.peek(Token![<=]) {
            let fork = input.fork();
            if let Ok(arguments) = fork.parse() {
                input.advance_to(&fork);
                return Ok(PathSegment {
                    ident,
                    arguments: PathArguments::AngleBracketed(arguments),
                });
            }
        }
        Ok(PathSegment::from(ident))
    }
}
```

</div>

##### <a href="#drawbacks" class="doc-anchor">§</a>Drawbacks

The main drawback of this style of speculative parsing is in error
presentation. Even if the lookahead is the “correct” parse, the error
that is shown is that of the “fallback” parse. To use the same example
as the turbofish above, take the following unfinished “turbofish”:

<div class="example-wrap">

``` text
let _ = f<&'a fn(), for<'a> serde::>();
```

</div>

If this is parsed as generic arguments, we can provide the error message

<div class="example-wrap">

``` text
error: expected identifier
 --> src.rs:L:C
  |
L | let _ = f<&'a fn(), for<'a> serde::>();
  |                                    ^
```

</div>

but if parsed using the above speculative parsing, it falls back to
assuming that the `<` is a less-than when it fails to parse the generic
arguments, and tries to interpret the `&'a` as the start of a labelled
loop, resulting in the much less helpful error

<div class="example-wrap">

``` text
error: expected `:`
 --> src.rs:L:C
  |
L | let _ = f<&'a fn(), for<'a> serde::>();
  |               ^^
```

</div>

This can be mitigated with various heuristics (two examples: show both
forks’ parse errors, or show the one that consumed more tokens), but
when you can control the grammar, sticking to something that can be
parsed LL(3) and without the LL(\*) speculative parsing this makes
possible, displaying reasonable errors becomes much more simple.

##### <a href="#performance" class="doc-anchor">§</a>Performance

This method performs a cheap fixed amount of work that does not depend
on how far apart the two streams are positioned.

##### <a href="#panics" class="doc-anchor">§</a>Panics

The forked stream in the argument of `advance_to` must have been
obtained by forking `self`. Attempting to advance to any other stream
will cause a panic.

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Speculative-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../../src/verus_syn/discouraged.rs.html#167-201"
class="src rightside">Source</a><a href="#impl-Speculative-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="trait.Speculative.html" class="trait"
title="trait verus_syn::parse::discouraged::Speculative">Speculative</a> for <a href="../struct.ParseBuffer.html" class="struct"
title="struct verus_syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

</div>

</div>

</div>
