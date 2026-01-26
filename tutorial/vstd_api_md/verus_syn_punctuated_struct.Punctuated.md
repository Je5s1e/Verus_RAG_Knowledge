<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[punctuated](index.html)

</div>

# Struct <span class="struct">Punctuated</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/punctuated.rs.html#49-52"
class="src">Source</a> </span>

</div>

``` rust
pub struct Punctuated<T, P> { /* private fields */ }
```

Expand description

<div class="docblock">

**A punctuated sequence of syntax tree nodes of type `T` separated by
punctuation of type `P`.**

Refer to the [module
documentation](index.html "mod verus_syn::punctuated") for details about
punctuated sequences.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#54-383"
class="src rightside">Source</a><a href="#impl-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#56-61"
class="src rightside">Source</a>

#### pub const fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Creates an empty punctuated sequence.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#65-67"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Determines whether this punctuated sequence is empty, meaning it
contains no syntax tree nodes or punctuation.

</div>

<div id="method.len" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#73-75"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of syntax tree nodes in this punctuated sequence.

This is the number of nodes of type `T`, not counting the punctuation of
type `P`.

</div>

<div id="method.first" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#78-80"
class="src rightside">Source</a>

#### pub fn <a href="#method.first" class="fn">first</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Borrows the first element in this sequence.

</div>

<div id="method.first_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#83-85"
class="src rightside">Source</a>

#### pub fn <a href="#method.first_mut" class="fn">first_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>\>

</div>

<div class="docblock">

Mutably borrows the first element in this sequence.

</div>

<div id="method.last" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#88-90"
class="src rightside">Source</a>

#### pub fn <a href="#method.last" class="fn">last</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Borrows the last element in this sequence.

</div>

<div id="method.last_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#93-95"
class="src rightside">Source</a>

#### pub fn <a href="#method.last_mut" class="fn">last_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>\>

</div>

<div class="docblock">

Mutably borrows the last element in this sequence.

</div>

<div id="method.get" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#98-106"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Borrows the element at the given index.

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#109-118"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>\>

</div>

<div class="docblock">

Mutably borrows the element at the given index.

</div>

<div id="method.iter" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#121-128"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="struct.Iter.html" class="struct"
title="struct verus_syn::punctuated::Iter">Iter</a>\<'\_, T\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;_, T&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over borrowed syntax tree nodes of type `&T`.

</div>

<div id="method.iter_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#132-139"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter_mut" class="fn">iter_mut</a>(&mut self) -\> <a href="struct.IterMut.html" class="struct"
title="struct verus_syn::punctuated::IterMut">IterMut</a>\<'\_, T\> <a href="#" class="tooltip"
data-notable-ty="IterMut&lt;&#39;_, T&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over mutably borrowed syntax tree nodes of type
`&mut T`.

</div>

<div id="method.pairs" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#143-148"
class="src rightside">Source</a>

#### pub fn <a href="#method.pairs" class="fn">pairs</a>(&self) -\> <a href="struct.Pairs.html" class="struct"
title="struct verus_syn::punctuated::Pairs">Pairs</a>\<'\_, T, P\> <a href="#" class="tooltip"
data-notable-ty="Pairs&lt;&#39;_, T, P&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over the contents of this sequence as borrowed
punctuated pairs.

</div>

<div id="method.pairs_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#152-157"
class="src rightside">Source</a>

#### pub fn <a href="#method.pairs_mut" class="fn">pairs_mut</a>(&mut self) -\> <a href="struct.PairsMut.html" class="struct"
title="struct verus_syn::punctuated::PairsMut">PairsMut</a>\<'\_, T, P\> <a href="#" class="tooltip"
data-notable-ty="PairsMut&lt;&#39;_, T, P&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over the contents of this sequence as mutably
borrowed punctuated pairs.

</div>

<div id="method.into_pairs" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#161-166"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_pairs" class="fn">into_pairs</a>(self) -\> <a href="struct.IntoPairs.html" class="struct"
title="struct verus_syn::punctuated::IntoPairs">IntoPairs</a>\<T, P\> <a href="#" class="tooltip"
data-notable-ty="IntoPairs&lt;T, P&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over the contents of this sequence as owned
punctuated pairs.

</div>

<div id="method.push_value" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#180-187"
class="src rightside">Source</a>

#### pub fn <a href="#method.push_value" class="fn">push_value</a>(&mut self, value: T)

</div>

<div class="docblock">

Appends a syntax tree node onto the end of this punctuated sequence. The
sequence must already have a trailing punctuation, or be empty.

Use
[`push`](struct.Punctuated.html#method.push "method verus_syn::punctuated::Punctuated::push")
instead if the punctuated sequence may or may not already have trailing
punctuation.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the sequence is nonempty and does not already have a trailing
punctuation.

</div>

<div id="method.push_punct" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#196-204"
class="src rightside">Source</a>

#### pub fn <a href="#method.push_punct" class="fn">push_punct</a>(&mut self, punctuation: P)

</div>

<div class="docblock">

Appends a trailing punctuation onto the end of this punctuated sequence.
The sequence must be non-empty and must not already have trailing
punctuation.

##### <a href="#panics-1" class="doc-anchor">§</a>Panics

Panics if the sequence is empty or already has a trailing punctuation.

</div>

<div id="method.pop" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#208-214"
class="src rightside">Source</a>

#### pub fn <a href="#method.pop" class="fn">pop</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\>

</div>

<div class="docblock">

Removes the last punctuated pair from this sequence, or `None` if the
sequence is empty.

</div>

<div id="method.pop_punct" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#218-226"
class="src rightside">Source</a>

#### pub fn <a href="#method.pop_punct" class="fn">pop_punct</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<P\>

</div>

<div class="docblock">

Removes the trailing punctuation from this punctuated sequence, or
`None` if there isn’t any.

</div>

<div id="method.trailing_punct" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#230-232"
class="src rightside">Source</a>

#### pub fn <a href="#method.trailing_punct" class="fn">trailing_punct</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Determines whether this punctuated sequence ends with a trailing
punctuation.

</div>

<div id="method.empty_or_trailing" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#238-240"
class="src rightside">Source</a>

#### pub fn <a href="#method.empty_or_trailing" class="fn">empty_or_trailing</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if either this `Punctuated` is empty, or it has a trailing
punctuation.

Equivalent to `punctuated.is_empty() || punctuated.trailing_punct()`.

</div>

<div id="method.push" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#247-255"
class="src rightside">Source</a>

#### pub fn <a href="#method.push" class="fn">push</a>(&mut self, value: T)

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="docblock">

Appends a syntax tree node onto the end of this punctuated sequence.

If there is not a trailing punctuation in this sequence when this method
is called, the default value of punctuation type `P` is inserted before
the given value of type `T`.

</div>

<div id="method.insert" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#263-277"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, value: T)

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="docblock">

Inserts an element at position `index`.

##### <a href="#panics-2" class="doc-anchor">§</a>Panics

Panics if `index` is greater than the number of elements previously in
this punctuated sequence.

</div>

<div id="method.clear" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#280-283"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Clears the sequence of all values and punctuation, making it empty.

</div>

<div id="method.parse_terminated" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#292-298"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_terminated" class="fn">parse_terminated</a>(input: <a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

<div class="where">

where T: <a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>, P:
<a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>,

</div>

</div>

<div class="docblock">

Parses zero or more occurrences of `T` separated by punctuation of type
`P`, with optional trailing punctuation.

Parsing continues until the end of this parse stream. The entire content
of this parse stream must consist of `T` and `P`.

</div>

<div id="method.parse_terminated_with" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#310-333"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_terminated_with"
class="fn">parse_terminated_with</a>\<'a\>( input: <a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'a\>, parser: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.fn.html"
class="primitive">fn</a>(<a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'a\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<T\>, ) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

<div class="where">

where P: <a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>,

</div>

</div>

<div class="docblock">

Parses zero or more occurrences of `T` using the given parse function,
separated by punctuation of type `P`, with optional trailing
punctuation.

Like
[`parse_terminated`](struct.Punctuated.html#method.parse_terminated "associated function verus_syn::punctuated::Punctuated::parse_terminated"),
the entire content of this stream is expected to be parsed.

</div>

<div id="method.parse_separated_nonempty" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#344-350"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_separated_nonempty"
class="fn">parse_separated_nonempty</a>(input: <a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

<div class="where">

where T: <a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>, P:
<a href="../token/trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> +
<a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>,

</div>

</div>

<div class="docblock">

Parses one or more occurrences of `T` separated by punctuation of type
`P`, not accepting trailing punctuation.

Parsing continues as long as punctuation `P` is present at the head of
the stream. This method returns upon parsing a `T` and observing that it
is not followed by a `P`, even if there are remaining tokens in the
stream.

</div>

<div id="method.parse_separated_nonempty_with" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#362-382"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_separated_nonempty_with"
class="fn">parse_separated_nonempty_with</a>\<'a\>( input: <a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'a\>, parser: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.fn.html"
class="primitive">fn</a>(<a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'a\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<T\>, ) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

<div class="where">

where P: <a href="../token/trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a> +
<a href="../parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>,

</div>

</div>

<div class="docblock">

Parses one or more occurrences of `T` using the given parse function,
separated by punctuation of type `P`, not accepting trailing
punctuation.

Like
[`parse_separated_nonempty`](struct.Punctuated.html#method.parse_separated_nonempty "associated function verus_syn::punctuated::Punctuated::parse_separated_nonempty"),
may complete early without parsing the entire content of this stream.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#387-403"
class="src rightside">Source</a><a href="#impl-Clone-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `clone-impls`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#392-397"
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

<a href="../../src/verus_syn/punctuated.rs.html#399-402"
class="src rightside">Source</a><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, other: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#443-455"
class="src rightside">Source</a><a href="#impl-Debug-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, P: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `extra-traits`** only.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#444-454"
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

<div id="impl-Default-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#556-560"
class="src rightside">Source</a><a href="#impl-Default-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.default" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#557-559"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Returns the “default value” for a type. [Read
more](https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default)

</div>

</div>

<div id="impl-Extend%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#487-497"
class="src rightside">Source</a><a href="#impl-Extend%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend-1" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#491-496"
class="src rightside">Source</a><a href="#method.extend-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\>\>(&mut self, i: I)

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

</div>

<div id="method.extend_one-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one-1" class="anchor">§</a>

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

<div id="method.extend_reserve-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve-1" class="anchor">§</a>

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

<div id="impl-Extend%3CT%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#468-477"
class="src rightside">Source</a><a href="#impl-Extend%3CT%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<T\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#472-476"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(&mut self, i: I)

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

<div id="impl-FromIterator%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#479-485"
class="src rightside">Source</a><a
href="#impl-FromIterator%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.from_iter-1" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#480-484"
class="src rightside">Source</a><a href="#method.from_iter-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\>\>(i: I) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-FromIterator%3CT%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#457-466"
class="src rightside">Source</a><a href="#impl-FromIterator%3CT%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<T\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.from_iter" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#461-465"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(i: I) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-Hash-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#429-439"
class="src rightside">Source</a><a href="#impl-Hash-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `extra-traits`** only.

</div>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#434-438"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<H: <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>\>(&self, state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

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

<div id="impl-Index%3Cusize%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1078-1091"
class="src rightside">Source</a><a href="#impl-Index%3Cusize%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html"
class="trait" title="trait core::ops::index::Index">Index</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1079"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype">Output</a> = T

</div>

<div class="docblock">

The returned type after indexing.

</div>

<div id="method.index" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1081-1090"
class="src rightside">Source</a><a href="#method.index" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index"
class="fn">index</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::index::Index::Output">Output</a>

</div>

<div class="docblock">

Performs the indexing (`container[index]`) operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index)

</div>

</div>

<div id="impl-IndexMut%3Cusize%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1093-1104"
class="src rightside">Source</a><a href="#impl-IndexMut%3Cusize%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html"
class="trait" title="trait core::ops::index::IndexMut">IndexMut</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.index_mut" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1094-1103"
class="src rightside">Source</a><a href="#method.index_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html#tymethod.index_mut"
class="fn">index_mut</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &mut Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::index::Index::Output">Output</a>

</div>

<div class="docblock">

Performs the mutable indexing (`container[index]`) operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html#tymethod.index_mut)

</div>

</div>

<div id="impl-IntoIterator-for-%26Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#538-545"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<'a, T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#539"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-1"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#540"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.Iter.html" class="struct"
title="struct verus_syn::punctuated::Iter">Iter</a>\<'a, T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#542-544"
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

<div id="impl-IntoIterator-for-%26mut+Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#547-554"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26mut+Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<'a, T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a mut <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="associatedtype.Item-2"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#548"
class="src rightside">Source</a><a href="#associatedtype.Item-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a mut T</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-2"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#549"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IterMut.html" class="struct"
title="struct verus_syn::punctuated::IterMut">IterMut</a>\<'a, T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-2" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#551-553"
class="src rightside">Source</a><a href="#method.into_iter-2" class="anchor">§</a>

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

<div id="impl-IntoIterator-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#518-536"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#519"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = T

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#520"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IntoIter.html" class="struct"
title="struct verus_syn::punctuated::IntoIter">IntoIter</a>\<T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#522-535"
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

<div id="impl-PartialEq-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#416-425"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `extra-traits`** only.

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#421-424"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
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

<div id="impl-ToTokens-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1143-1151"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, P:
<a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1148-1150"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a
href="../../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Eq-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#407-412"
class="src rightside">Source</a><a href="#impl-Eq-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `extra-traits`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="#impl-Freeze-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div id="impl-RefUnwindSafe-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
P: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="#impl-Send-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="#impl-Sync-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="#impl-Unpin-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-Punctuated%3CT,+P%3E" class="section impl">

<a href="#impl-UnwindSafe-for-Punctuated%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>,

</div>

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

<div id="impl-Spanned-for-T" class="section impl">

<a href="../../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="../spanned/trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span" class="section method trait-impl">

<a href="../../src/verus_syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span" class="anchor">§</a>

#### fn <a href="../spanned/trait.Spanned.html#tymethod.span"
class="fn">span</a>(&self) -\> <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
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
