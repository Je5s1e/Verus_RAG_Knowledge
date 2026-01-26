<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[visit](index.html)

</div>

# Trait <span class="trait">Visit</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/gen/visit.rs.html#28-1154"
class="src">Source</a> </span>

</div>

``` rust
pub trait Visit<'ast> {
Show 257 methods    // Provided methods
    fn visit_abi(&mut self, i: &'ast Abi) { ... }
    fn visit_angle_bracketed_generic_arguments(
        &mut self,
        i: &'ast AngleBracketedGenericArguments,
    ) { ... }
    fn visit_arm(&mut self, i: &'ast Arm) { ... }
    fn visit_assert(&mut self, i: &'ast Assert) { ... }
    fn visit_assert_forall(&mut self, i: &'ast AssertForall) { ... }
    fn visit_assoc_const(&mut self, i: &'ast AssocConst) { ... }
    fn visit_assoc_type(&mut self, i: &'ast AssocType) { ... }
    fn visit_assume(&mut self, i: &'ast Assume) { ... }
    fn visit_assume_specification(&mut self, i: &'ast AssumeSpecification) { ... }
    fn visit_attr_style(&mut self, i: &'ast AttrStyle) { ... }
    fn visit_attribute(&mut self, i: &'ast Attribute) { ... }
    fn visit_bare_fn_arg(&mut self, i: &'ast BareFnArg) { ... }
    fn visit_bare_variadic(&mut self, i: &'ast BareVariadic) { ... }
    fn visit_big_and(&mut self, i: &'ast BigAnd) { ... }
    fn visit_big_and_expr(&mut self, i: &'ast BigAndExpr) { ... }
    fn visit_big_or(&mut self, i: &'ast BigOr) { ... }
    fn visit_big_or_expr(&mut self, i: &'ast BigOrExpr) { ... }
    fn visit_bin_op(&mut self, i: &'ast BinOp) { ... }
    fn visit_block(&mut self, i: &'ast Block) { ... }
    fn visit_bound_lifetimes(&mut self, i: &'ast BoundLifetimes) { ... }
    fn visit_broadcast_use(&mut self, i: &'ast BroadcastUse) { ... }
    fn visit_captured_param(&mut self, i: &'ast CapturedParam) { ... }
    fn visit_closed(&mut self, i: &'ast Closed) { ... }
    fn visit_closure_arg(&mut self, i: &'ast ClosureArg) { ... }
    fn visit_const_param(&mut self, i: &'ast ConstParam) { ... }
    fn visit_constraint(&mut self, i: &'ast Constraint) { ... }
    fn visit_data(&mut self, i: &'ast Data) { ... }
    fn visit_data_enum(&mut self, i: &'ast DataEnum) { ... }
    fn visit_data_mode(&mut self, i: &'ast DataMode) { ... }
    fn visit_data_struct(&mut self, i: &'ast DataStruct) { ... }
    fn visit_data_union(&mut self, i: &'ast DataUnion) { ... }
    fn visit_decreases(&mut self, i: &'ast Decreases) { ... }
    fn visit_default_ensures(&mut self, i: &'ast DefaultEnsures) { ... }
    fn visit_derive_input(&mut self, i: &'ast DeriveInput) { ... }
    fn visit_ensures(&mut self, i: &'ast Ensures) { ... }
    fn visit_expr(&mut self, i: &'ast Expr) { ... }
    fn visit_expr_array(&mut self, i: &'ast ExprArray) { ... }
    fn visit_expr_assign(&mut self, i: &'ast ExprAssign) { ... }
    fn visit_expr_async(&mut self, i: &'ast ExprAsync) { ... }
    fn visit_expr_await(&mut self, i: &'ast ExprAwait) { ... }
    fn visit_expr_binary(&mut self, i: &'ast ExprBinary) { ... }
    fn visit_expr_block(&mut self, i: &'ast ExprBlock) { ... }
    fn visit_expr_break(&mut self, i: &'ast ExprBreak) { ... }
    fn visit_expr_call(&mut self, i: &'ast ExprCall) { ... }
    fn visit_expr_cast(&mut self, i: &'ast ExprCast) { ... }
    fn visit_expr_closure(&mut self, i: &'ast ExprClosure) { ... }
    fn visit_expr_const(&mut self, i: &'ast ExprConst) { ... }
    fn visit_expr_continue(&mut self, i: &'ast ExprContinue) { ... }
    fn visit_expr_field(&mut self, i: &'ast ExprField) { ... }
    fn visit_expr_for_loop(&mut self, i: &'ast ExprForLoop) { ... }
    fn visit_expr_get_field(&mut self, i: &'ast ExprGetField) { ... }
    fn visit_expr_group(&mut self, i: &'ast ExprGroup) { ... }
    fn visit_expr_has(&mut self, i: &'ast ExprHas) { ... }
    fn visit_expr_has_not(&mut self, i: &'ast ExprHasNot) { ... }
    fn visit_expr_if(&mut self, i: &'ast ExprIf) { ... }
    fn visit_expr_index(&mut self, i: &'ast ExprIndex) { ... }
    fn visit_expr_infer(&mut self, i: &'ast ExprInfer) { ... }
    fn visit_expr_is(&mut self, i: &'ast ExprIs) { ... }
    fn visit_expr_is_not(&mut self, i: &'ast ExprIsNot) { ... }
    fn visit_expr_let(&mut self, i: &'ast ExprLet) { ... }
    fn visit_expr_lit(&mut self, i: &'ast ExprLit) { ... }
    fn visit_expr_loop(&mut self, i: &'ast ExprLoop) { ... }
    fn visit_expr_macro(&mut self, i: &'ast ExprMacro) { ... }
    fn visit_expr_match(&mut self, i: &'ast ExprMatch) { ... }
    fn visit_expr_matches(&mut self, i: &'ast ExprMatches) { ... }
    fn visit_expr_method_call(&mut self, i: &'ast ExprMethodCall) { ... }
    fn visit_expr_paren(&mut self, i: &'ast ExprParen) { ... }
    fn visit_expr_path(&mut self, i: &'ast ExprPath) { ... }
    fn visit_expr_range(&mut self, i: &'ast ExprRange) { ... }
    fn visit_expr_raw_addr(&mut self, i: &'ast ExprRawAddr) { ... }
    fn visit_expr_reference(&mut self, i: &'ast ExprReference) { ... }
    fn visit_expr_repeat(&mut self, i: &'ast ExprRepeat) { ... }
    fn visit_expr_return(&mut self, i: &'ast ExprReturn) { ... }
    fn visit_expr_struct(&mut self, i: &'ast ExprStruct) { ... }
    fn visit_expr_try(&mut self, i: &'ast ExprTry) { ... }
    fn visit_expr_try_block(&mut self, i: &'ast ExprTryBlock) { ... }
    fn visit_expr_tuple(&mut self, i: &'ast ExprTuple) { ... }
    fn visit_expr_unary(&mut self, i: &'ast ExprUnary) { ... }
    fn visit_expr_unsafe(&mut self, i: &'ast ExprUnsafe) { ... }
    fn visit_expr_while(&mut self, i: &'ast ExprWhile) { ... }
    fn visit_expr_yield(&mut self, i: &'ast ExprYield) { ... }
    fn visit_field(&mut self, i: &'ast Field) { ... }
    fn visit_field_mutability(&mut self, i: &'ast FieldMutability) { ... }
    fn visit_field_pat(&mut self, i: &'ast FieldPat) { ... }
    fn visit_field_value(&mut self, i: &'ast FieldValue) { ... }
    fn visit_fields(&mut self, i: &'ast Fields) { ... }
    fn visit_fields_named(&mut self, i: &'ast FieldsNamed) { ... }
    fn visit_fields_unnamed(&mut self, i: &'ast FieldsUnnamed) { ... }
    fn visit_file(&mut self, i: &'ast File) { ... }
    fn visit_fn_arg(&mut self, i: &'ast FnArg) { ... }
    fn visit_fn_arg_kind(&mut self, i: &'ast FnArgKind) { ... }
    fn visit_fn_mode(&mut self, i: &'ast FnMode) { ... }
    fn visit_fn_proof_arg(&mut self, i: &'ast FnProofArg) { ... }
    fn visit_fn_proof_options(&mut self, i: &'ast FnProofOptions) { ... }
    fn visit_foreign_item(&mut self, i: &'ast ForeignItem) { ... }
    fn visit_foreign_item_fn(&mut self, i: &'ast ForeignItemFn) { ... }
    fn visit_foreign_item_macro(&mut self, i: &'ast ForeignItemMacro) { ... }
    fn visit_foreign_item_static(&mut self, i: &'ast ForeignItemStatic) { ... }
    fn visit_foreign_item_type(&mut self, i: &'ast ForeignItemType) { ... }
    fn visit_generic_argument(&mut self, i: &'ast GenericArgument) { ... }
    fn visit_generic_param(&mut self, i: &'ast GenericParam) { ... }
    fn visit_generics(&mut self, i: &'ast Generics) { ... }
    fn visit_global(&mut self, i: &'ast Global) { ... }
    fn visit_global_inner(&mut self, i: &'ast GlobalInner) { ... }
    fn visit_global_layout(&mut self, i: &'ast GlobalLayout) { ... }
    fn visit_global_size_of(&mut self, i: &'ast GlobalSizeOf) { ... }
    fn visit_ident(&mut self, i: &'ast Ident) { ... }
    fn visit_impl_item(&mut self, i: &'ast ImplItem) { ... }
    fn visit_impl_item_const(&mut self, i: &'ast ImplItemConst) { ... }
    fn visit_impl_item_fn(&mut self, i: &'ast ImplItemFn) { ... }
    fn visit_impl_item_macro(&mut self, i: &'ast ImplItemMacro) { ... }
    fn visit_impl_item_type(&mut self, i: &'ast ImplItemType) { ... }
    fn visit_impl_restriction(&mut self, i: &'ast ImplRestriction) { ... }
    fn visit_index(&mut self, i: &'ast Index) { ... }
    fn visit_invariant(&mut self, i: &'ast Invariant) { ... }
    fn visit_invariant_ensures(&mut self, i: &'ast InvariantEnsures) { ... }
    fn visit_invariant_except_break(&mut self, i: &'ast InvariantExceptBreak) { ... }
    fn visit_invariant_name_set(&mut self, i: &'ast InvariantNameSet) { ... }
    fn visit_invariant_name_set_any(&mut self, i: &'ast InvariantNameSetAny) { ... }
    fn visit_invariant_name_set_list(&mut self, i: &'ast InvariantNameSetList) { ... }
    fn visit_invariant_name_set_none(&mut self, i: &'ast InvariantNameSetNone) { ... }
    fn visit_invariant_name_set_set(&mut self, i: &'ast InvariantNameSetSet) { ... }
    fn visit_item(&mut self, i: &'ast Item) { ... }
    fn visit_item_broadcast_group(&mut self, i: &'ast ItemBroadcastGroup) { ... }
    fn visit_item_const(&mut self, i: &'ast ItemConst) { ... }
    fn visit_item_enum(&mut self, i: &'ast ItemEnum) { ... }
    fn visit_item_extern_crate(&mut self, i: &'ast ItemExternCrate) { ... }
    fn visit_item_fn(&mut self, i: &'ast ItemFn) { ... }
    fn visit_item_foreign_mod(&mut self, i: &'ast ItemForeignMod) { ... }
    fn visit_item_impl(&mut self, i: &'ast ItemImpl) { ... }
    fn visit_item_macro(&mut self, i: &'ast ItemMacro) { ... }
    fn visit_item_mod(&mut self, i: &'ast ItemMod) { ... }
    fn visit_item_static(&mut self, i: &'ast ItemStatic) { ... }
    fn visit_item_struct(&mut self, i: &'ast ItemStruct) { ... }
    fn visit_item_trait(&mut self, i: &'ast ItemTrait) { ... }
    fn visit_item_trait_alias(&mut self, i: &'ast ItemTraitAlias) { ... }
    fn visit_item_type(&mut self, i: &'ast ItemType) { ... }
    fn visit_item_union(&mut self, i: &'ast ItemUnion) { ... }
    fn visit_item_use(&mut self, i: &'ast ItemUse) { ... }
    fn visit_label(&mut self, i: &'ast Label) { ... }
    fn visit_lifetime(&mut self, i: &'ast Lifetime) { ... }
    fn visit_lifetime_param(&mut self, i: &'ast LifetimeParam) { ... }
    fn visit_lit(&mut self, i: &'ast Lit) { ... }
    fn visit_lit_bool(&mut self, i: &'ast LitBool) { ... }
    fn visit_lit_byte(&mut self, i: &'ast LitByte) { ... }
    fn visit_lit_byte_str(&mut self, i: &'ast LitByteStr) { ... }
    fn visit_lit_cstr(&mut self, i: &'ast LitCStr) { ... }
    fn visit_lit_char(&mut self, i: &'ast LitChar) { ... }
    fn visit_lit_float(&mut self, i: &'ast LitFloat) { ... }
    fn visit_lit_int(&mut self, i: &'ast LitInt) { ... }
    fn visit_lit_str(&mut self, i: &'ast LitStr) { ... }
    fn visit_local(&mut self, i: &'ast Local) { ... }
    fn visit_local_init(&mut self, i: &'ast LocalInit) { ... }
    fn visit_loop_spec(&mut self, i: &'ast LoopSpec) { ... }
    fn visit_macro(&mut self, i: &'ast Macro) { ... }
    fn visit_macro_delimiter(&mut self, i: &'ast MacroDelimiter) { ... }
    fn visit_matches_op_expr(&mut self, i: &'ast MatchesOpExpr) { ... }
    fn visit_matches_op_token(&mut self, i: &'ast MatchesOpToken) { ... }
    fn visit_member(&mut self, i: &'ast Member) { ... }
    fn visit_meta(&mut self, i: &'ast Meta) { ... }
    fn visit_meta_list(&mut self, i: &'ast MetaList) { ... }
    fn visit_meta_name_value(&mut self, i: &'ast MetaNameValue) { ... }
    fn visit_mode(&mut self, i: &'ast Mode) { ... }
    fn visit_mode_exec(&mut self, i: &'ast ModeExec) { ... }
    fn visit_mode_ghost(&mut self, i: &'ast ModeGhost) { ... }
    fn visit_mode_proof(&mut self, i: &'ast ModeProof) { ... }
    fn visit_mode_proof_axiom(&mut self, i: &'ast ModeProofAxiom) { ... }
    fn visit_mode_spec(&mut self, i: &'ast ModeSpec) { ... }
    fn visit_mode_spec_checked(&mut self, i: &'ast ModeSpecChecked) { ... }
    fn visit_mode_tracked(&mut self, i: &'ast ModeTracked) { ... }
    fn visit_open(&mut self, i: &'ast Open) { ... }
    fn visit_open_restricted(&mut self, i: &'ast OpenRestricted) { ... }
    fn visit_parenthesized_generic_arguments(
        &mut self,
        i: &'ast ParenthesizedGenericArguments,
    ) { ... }
    fn visit_pat(&mut self, i: &'ast Pat) { ... }
    fn visit_pat_ident(&mut self, i: &'ast PatIdent) { ... }
    fn visit_pat_or(&mut self, i: &'ast PatOr) { ... }
    fn visit_pat_paren(&mut self, i: &'ast PatParen) { ... }
    fn visit_pat_reference(&mut self, i: &'ast PatReference) { ... }
    fn visit_pat_rest(&mut self, i: &'ast PatRest) { ... }
    fn visit_pat_slice(&mut self, i: &'ast PatSlice) { ... }
    fn visit_pat_struct(&mut self, i: &'ast PatStruct) { ... }
    fn visit_pat_tuple(&mut self, i: &'ast PatTuple) { ... }
    fn visit_pat_tuple_struct(&mut self, i: &'ast PatTupleStruct) { ... }
    fn visit_pat_type(&mut self, i: &'ast PatType) { ... }
    fn visit_pat_wild(&mut self, i: &'ast PatWild) { ... }
    fn visit_path(&mut self, i: &'ast Path) { ... }
    fn visit_path_arguments(&mut self, i: &'ast PathArguments) { ... }
    fn visit_path_segment(&mut self, i: &'ast PathSegment) { ... }
    fn visit_pointer_mutability(&mut self, i: &'ast PointerMutability) { ... }
    fn visit_precise_capture(&mut self, i: &'ast PreciseCapture) { ... }
    fn visit_predicate_lifetime(&mut self, i: &'ast PredicateLifetime) { ... }
    fn visit_predicate_type(&mut self, i: &'ast PredicateType) { ... }
    fn visit_prover(&mut self, i: &'ast Prover) { ... }
    fn visit_publish(&mut self, i: &'ast Publish) { ... }
    fn visit_qself(&mut self, i: &'ast QSelf) { ... }
    fn visit_range_limits(&mut self, i: &'ast RangeLimits) { ... }
    fn visit_receiver(&mut self, i: &'ast Receiver) { ... }
    fn visit_recommends(&mut self, i: &'ast Recommends) { ... }
    fn visit_requires(&mut self, i: &'ast Requires) { ... }
    fn visit_return_type(&mut self, i: &'ast ReturnType) { ... }
    fn visit_returns(&mut self, i: &'ast Returns) { ... }
    fn visit_reveal_hide(&mut self, i: &'ast RevealHide) { ... }
    fn visit_signature(&mut self, i: &'ast Signature) { ... }
    fn visit_signature_decreases(&mut self, i: &'ast SignatureDecreases) { ... }
    fn visit_signature_invariants(&mut self, i: &'ast SignatureInvariants) { ... }
    fn visit_signature_spec(&mut self, i: &'ast SignatureSpec) { ... }
    fn visit_signature_spec_attr(&mut self, i: &'ast SignatureSpecAttr) { ... }
    fn visit_signature_unwind(&mut self, i: &'ast SignatureUnwind) { ... }
    fn visit_span(&mut self, i: &Span) { ... }
    fn visit_specification(&mut self, i: &'ast Specification) { ... }
    fn visit_static_mutability(&mut self, i: &'ast StaticMutability) { ... }
    fn visit_stmt(&mut self, i: &'ast Stmt) { ... }
    fn visit_stmt_macro(&mut self, i: &'ast StmtMacro) { ... }
    fn visit_token_stream(&mut self, i: &'ast TokenStream) { ... }
    fn visit_trait_bound(&mut self, i: &'ast TraitBound) { ... }
    fn visit_trait_bound_modifier(&mut self, i: &'ast TraitBoundModifier) { ... }
    fn visit_trait_item(&mut self, i: &'ast TraitItem) { ... }
    fn visit_trait_item_const(&mut self, i: &'ast TraitItemConst) { ... }
    fn visit_trait_item_fn(&mut self, i: &'ast TraitItemFn) { ... }
    fn visit_trait_item_macro(&mut self, i: &'ast TraitItemMacro) { ... }
    fn visit_trait_item_type(&mut self, i: &'ast TraitItemType) { ... }
    fn visit_type(&mut self, i: &'ast Type) { ... }
    fn visit_type_array(&mut self, i: &'ast TypeArray) { ... }
    fn visit_type_bare_fn(&mut self, i: &'ast TypeBareFn) { ... }
    fn visit_type_fn_proof(&mut self, i: &'ast TypeFnProof) { ... }
    fn visit_type_fn_spec(&mut self, i: &'ast TypeFnSpec) { ... }
    fn visit_type_group(&mut self, i: &'ast TypeGroup) { ... }
    fn visit_type_impl_trait(&mut self, i: &'ast TypeImplTrait) { ... }
    fn visit_type_infer(&mut self, i: &'ast TypeInfer) { ... }
    fn visit_type_macro(&mut self, i: &'ast TypeMacro) { ... }
    fn visit_type_never(&mut self, i: &'ast TypeNever) { ... }
    fn visit_type_param(&mut self, i: &'ast TypeParam) { ... }
    fn visit_type_param_bound(&mut self, i: &'ast TypeParamBound) { ... }
    fn visit_type_paren(&mut self, i: &'ast TypeParen) { ... }
    fn visit_type_path(&mut self, i: &'ast TypePath) { ... }
    fn visit_type_ptr(&mut self, i: &'ast TypePtr) { ... }
    fn visit_type_reference(&mut self, i: &'ast TypeReference) { ... }
    fn visit_type_slice(&mut self, i: &'ast TypeSlice) { ... }
    fn visit_type_trait_object(&mut self, i: &'ast TypeTraitObject) { ... }
    fn visit_type_tuple(&mut self, i: &'ast TypeTuple) { ... }
    fn visit_un_op(&mut self, i: &'ast UnOp) { ... }
    fn visit_uninterp(&mut self, i: &'ast Uninterp) { ... }
    fn visit_use_glob(&mut self, i: &'ast UseGlob) { ... }
    fn visit_use_group(&mut self, i: &'ast UseGroup) { ... }
    fn visit_use_name(&mut self, i: &'ast UseName) { ... }
    fn visit_use_path(&mut self, i: &'ast UsePath) { ... }
    fn visit_use_rename(&mut self, i: &'ast UseRename) { ... }
    fn visit_use_tree(&mut self, i: &'ast UseTree) { ... }
    fn visit_variadic(&mut self, i: &'ast Variadic) { ... }
    fn visit_variant(&mut self, i: &'ast Variant) { ... }
    fn visit_view(&mut self, i: &'ast View) { ... }
    fn visit_vis_restricted(&mut self, i: &'ast VisRestricted) { ... }
    fn visit_visibility(&mut self, i: &'ast Visibility) { ... }
    fn visit_where_clause(&mut self, i: &'ast WhereClause) { ... }
    fn visit_where_predicate(&mut self, i: &'ast WherePredicate) { ... }
    fn visit_with_spec_on_expr(&mut self, i: &'ast WithSpecOnExpr) { ... }
    fn visit_with_spec_on_fn(&mut self, i: &'ast WithSpecOnFn) { ... }
}
```

Expand description

<div class="docblock">

Syntax tree traversal to walk a shared borrow of a syntax tree.

See the [module documentation](index.html "mod verus_syn::visit") for
details.

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.visit_abi" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#31-33"
class="src rightside">Source</a>

#### fn <a href="#method.visit_abi" class="fn">visit_abi</a>(&mut self, i: &'ast <a href="../struct.Abi.html" class="struct"
title="struct verus_syn::Abi">Abi</a>)

</div>

<div id="method.visit_angle_bracketed_generic_arguments"
class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#36-41"
class="src rightside">Source</a>

#### fn <a href="#method.visit_angle_bracketed_generic_arguments"
class="fn">visit_angle_bracketed_generic_arguments</a>( &mut self, i: &'ast <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct verus_syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>, )

</div>

<div id="method.visit_arm" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#44-46"
class="src rightside">Source</a>

#### fn <a href="#method.visit_arm" class="fn">visit_arm</a>(&mut self, i: &'ast <a href="../struct.Arm.html" class="struct"
title="struct verus_syn::Arm">Arm</a>)

</div>

<div id="method.visit_assert" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#47-49"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assert" class="fn">visit_assert</a>(&mut self, i: &'ast <a href="../struct.Assert.html" class="struct"
title="struct verus_syn::Assert">Assert</a>)

</div>

<div id="method.visit_assert_forall" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#50-52"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assert_forall" class="fn">visit_assert_forall</a>(&mut self, i: &'ast <a href="../struct.AssertForall.html" class="struct"
title="struct verus_syn::AssertForall">AssertForall</a>)

</div>

<div id="method.visit_assoc_const" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#55-57"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_const" class="fn">visit_assoc_const</a>(&mut self, i: &'ast <a href="../struct.AssocConst.html" class="struct"
title="struct verus_syn::AssocConst">AssocConst</a>)

</div>

<div id="method.visit_assoc_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#60-62"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_type" class="fn">visit_assoc_type</a>(&mut self, i: &'ast <a href="../struct.AssocType.html" class="struct"
title="struct verus_syn::AssocType">AssocType</a>)

</div>

<div id="method.visit_assume" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#63-65"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assume" class="fn">visit_assume</a>(&mut self, i: &'ast <a href="../struct.Assume.html" class="struct"
title="struct verus_syn::Assume">Assume</a>)

</div>

<div id="method.visit_assume_specification" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#66-68"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assume_specification"
class="fn">visit_assume_specification</a>(&mut self, i: &'ast <a href="../struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::AssumeSpecification">AssumeSpecification</a>)

</div>

<div id="method.visit_attr_style" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#71-73"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attr_style" class="fn">visit_attr_style</a>(&mut self, i: &'ast <a href="../enum.AttrStyle.html" class="enum"
title="enum verus_syn::AttrStyle">AttrStyle</a>)

</div>

<div id="method.visit_attribute" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#76-78"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attribute" class="fn">visit_attribute</a>(&mut self, i: &'ast <a href="../struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>)

</div>

<div id="method.visit_bare_fn_arg" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#81-83"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_fn_arg" class="fn">visit_bare_fn_arg</a>(&mut self, i: &'ast <a href="../struct.BareFnArg.html" class="struct"
title="struct verus_syn::BareFnArg">BareFnArg</a>)

</div>

<div id="method.visit_bare_variadic" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#86-88"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_variadic" class="fn">visit_bare_variadic</a>(&mut self, i: &'ast <a href="../struct.BareVariadic.html" class="struct"
title="struct verus_syn::BareVariadic">BareVariadic</a>)

</div>

<div id="method.visit_big_and" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#89-91"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_and" class="fn">visit_big_and</a>(&mut self, i: &'ast <a href="../struct.BigAnd.html" class="struct"
title="struct verus_syn::BigAnd">BigAnd</a>)

</div>

<div id="method.visit_big_and_expr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#92-94"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_and_expr" class="fn">visit_big_and_expr</a>(&mut self, i: &'ast <a href="../struct.BigAndExpr.html" class="struct"
title="struct verus_syn::BigAndExpr">BigAndExpr</a>)

</div>

<div id="method.visit_big_or" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#95-97"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_or" class="fn">visit_big_or</a>(&mut self, i: &'ast <a href="../struct.BigOr.html" class="struct"
title="struct verus_syn::BigOr">BigOr</a>)

</div>

<div id="method.visit_big_or_expr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#98-100"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_or_expr" class="fn">visit_big_or_expr</a>(&mut self, i: &'ast <a href="../struct.BigOrExpr.html" class="struct"
title="struct verus_syn::BigOrExpr">BigOrExpr</a>)

</div>

<div id="method.visit_bin_op" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#103-105"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bin_op" class="fn">visit_bin_op</a>(&mut self, i: &'ast <a href="../enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>)

</div>

<div id="method.visit_block" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#108-110"
class="src rightside">Source</a>

#### fn <a href="#method.visit_block" class="fn">visit_block</a>(&mut self, i: &'ast <a href="../struct.Block.html" class="struct"
title="struct verus_syn::Block">Block</a>)

</div>

<div id="method.visit_bound_lifetimes" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#113-115"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bound_lifetimes"
class="fn">visit_bound_lifetimes</a>(&mut self, i: &'ast <a href="../struct.BoundLifetimes.html" class="struct"
title="struct verus_syn::BoundLifetimes">BoundLifetimes</a>)

</div>

<div id="method.visit_broadcast_use" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#116-118"
class="src rightside">Source</a>

#### fn <a href="#method.visit_broadcast_use" class="fn">visit_broadcast_use</a>(&mut self, i: &'ast <a href="../struct.BroadcastUse.html" class="struct"
title="struct verus_syn::BroadcastUse">BroadcastUse</a>)

</div>

<div id="method.visit_captured_param" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#121-123"
class="src rightside">Source</a>

#### fn <a href="#method.visit_captured_param"
class="fn">visit_captured_param</a>(&mut self, i: &'ast <a href="../enum.CapturedParam.html" class="enum"
title="enum verus_syn::CapturedParam">CapturedParam</a>)

</div>

<div id="method.visit_closed" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#124-126"
class="src rightside">Source</a>

#### fn <a href="#method.visit_closed" class="fn">visit_closed</a>(&mut self, i: &'ast <a href="../struct.Closed.html" class="struct"
title="struct verus_syn::Closed">Closed</a>)

</div>

<div id="method.visit_closure_arg" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#127-129"
class="src rightside">Source</a>

#### fn <a href="#method.visit_closure_arg" class="fn">visit_closure_arg</a>(&mut self, i: &'ast <a href="../struct.ClosureArg.html" class="struct"
title="struct verus_syn::ClosureArg">ClosureArg</a>)

</div>

<div id="method.visit_const_param" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#132-134"
class="src rightside">Source</a>

#### fn <a href="#method.visit_const_param" class="fn">visit_const_param</a>(&mut self, i: &'ast <a href="../struct.ConstParam.html" class="struct"
title="struct verus_syn::ConstParam">ConstParam</a>)

</div>

<div id="method.visit_constraint" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#137-139"
class="src rightside">Source</a>

#### fn <a href="#method.visit_constraint" class="fn">visit_constraint</a>(&mut self, i: &'ast <a href="../struct.Constraint.html" class="struct"
title="struct verus_syn::Constraint">Constraint</a>)

</div>

<div id="method.visit_data" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#142-144"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data" class="fn">visit_data</a>(&mut self, i: &'ast <a href="../enum.Data.html" class="enum"
title="enum verus_syn::Data">Data</a>)

</div>

<div id="method.visit_data_enum" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#147-149"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_enum" class="fn">visit_data_enum</a>(&mut self, i: &'ast <a href="../struct.DataEnum.html" class="struct"
title="struct verus_syn::DataEnum">DataEnum</a>)

</div>

<div id="method.visit_data_mode" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#150-152"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_mode" class="fn">visit_data_mode</a>(&mut self, i: &'ast <a href="../enum.DataMode.html" class="enum"
title="enum verus_syn::DataMode">DataMode</a>)

</div>

<div id="method.visit_data_struct" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#155-157"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_struct" class="fn">visit_data_struct</a>(&mut self, i: &'ast <a href="../struct.DataStruct.html" class="struct"
title="struct verus_syn::DataStruct">DataStruct</a>)

</div>

<div id="method.visit_data_union" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#160-162"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_union" class="fn">visit_data_union</a>(&mut self, i: &'ast <a href="../struct.DataUnion.html" class="struct"
title="struct verus_syn::DataUnion">DataUnion</a>)

</div>

<div id="method.visit_decreases" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#163-165"
class="src rightside">Source</a>

#### fn <a href="#method.visit_decreases" class="fn">visit_decreases</a>(&mut self, i: &'ast <a href="../struct.Decreases.html" class="struct"
title="struct verus_syn::Decreases">Decreases</a>)

</div>

<div id="method.visit_default_ensures" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#166-168"
class="src rightside">Source</a>

#### fn <a href="#method.visit_default_ensures"
class="fn">visit_default_ensures</a>(&mut self, i: &'ast <a href="../struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::DefaultEnsures">DefaultEnsures</a>)

</div>

<div id="method.visit_derive_input" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#171-173"
class="src rightside">Source</a>

#### fn <a href="#method.visit_derive_input" class="fn">visit_derive_input</a>(&mut self, i: &'ast <a href="../struct.DeriveInput.html" class="struct"
title="struct verus_syn::DeriveInput">DeriveInput</a>)

</div>

<div id="method.visit_ensures" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#174-176"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ensures" class="fn">visit_ensures</a>(&mut self, i: &'ast <a href="../struct.Ensures.html" class="struct"
title="struct verus_syn::Ensures">Ensures</a>)

</div>

<div id="method.visit_expr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#179-181"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr" class="fn">visit_expr</a>(&mut self, i: &'ast <a href="../enum.Expr.html" class="enum"
title="enum verus_syn::Expr">Expr</a>)

</div>

<div id="method.visit_expr_array" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#184-186"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_array" class="fn">visit_expr_array</a>(&mut self, i: &'ast <a href="../struct.ExprArray.html" class="struct"
title="struct verus_syn::ExprArray">ExprArray</a>)

</div>

<div id="method.visit_expr_assign" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#189-191"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_assign" class="fn">visit_expr_assign</a>(&mut self, i: &'ast <a href="../struct.ExprAssign.html" class="struct"
title="struct verus_syn::ExprAssign">ExprAssign</a>)

</div>

<div id="method.visit_expr_async" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#194-196"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_async" class="fn">visit_expr_async</a>(&mut self, i: &'ast <a href="../struct.ExprAsync.html" class="struct"
title="struct verus_syn::ExprAsync">ExprAsync</a>)

</div>

<div id="method.visit_expr_await" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#199-201"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_await" class="fn">visit_expr_await</a>(&mut self, i: &'ast <a href="../struct.ExprAwait.html" class="struct"
title="struct verus_syn::ExprAwait">ExprAwait</a>)

</div>

<div id="method.visit_expr_binary" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#204-206"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_binary" class="fn">visit_expr_binary</a>(&mut self, i: &'ast <a href="../struct.ExprBinary.html" class="struct"
title="struct verus_syn::ExprBinary">ExprBinary</a>)

</div>

<div id="method.visit_expr_block" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#209-211"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_block" class="fn">visit_expr_block</a>(&mut self, i: &'ast <a href="../struct.ExprBlock.html" class="struct"
title="struct verus_syn::ExprBlock">ExprBlock</a>)

</div>

<div id="method.visit_expr_break" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#214-216"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_break" class="fn">visit_expr_break</a>(&mut self, i: &'ast <a href="../struct.ExprBreak.html" class="struct"
title="struct verus_syn::ExprBreak">ExprBreak</a>)

</div>

<div id="method.visit_expr_call" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#219-221"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_call" class="fn">visit_expr_call</a>(&mut self, i: &'ast <a href="../struct.ExprCall.html" class="struct"
title="struct verus_syn::ExprCall">ExprCall</a>)

</div>

<div id="method.visit_expr_cast" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#224-226"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_cast" class="fn">visit_expr_cast</a>(&mut self, i: &'ast <a href="../struct.ExprCast.html" class="struct"
title="struct verus_syn::ExprCast">ExprCast</a>)

</div>

<div id="method.visit_expr_closure" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#229-231"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_closure" class="fn">visit_expr_closure</a>(&mut self, i: &'ast <a href="../struct.ExprClosure.html" class="struct"
title="struct verus_syn::ExprClosure">ExprClosure</a>)

</div>

<div id="method.visit_expr_const" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#234-236"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_const" class="fn">visit_expr_const</a>(&mut self, i: &'ast <a href="../struct.ExprConst.html" class="struct"
title="struct verus_syn::ExprConst">ExprConst</a>)

</div>

<div id="method.visit_expr_continue" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#239-241"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_continue" class="fn">visit_expr_continue</a>(&mut self, i: &'ast <a href="../struct.ExprContinue.html" class="struct"
title="struct verus_syn::ExprContinue">ExprContinue</a>)

</div>

<div id="method.visit_expr_field" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#244-246"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_field" class="fn">visit_expr_field</a>(&mut self, i: &'ast <a href="../struct.ExprField.html" class="struct"
title="struct verus_syn::ExprField">ExprField</a>)

</div>

<div id="method.visit_expr_for_loop" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#249-251"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_for_loop" class="fn">visit_expr_for_loop</a>(&mut self, i: &'ast <a href="../struct.ExprForLoop.html" class="struct"
title="struct verus_syn::ExprForLoop">ExprForLoop</a>)

</div>

<div id="method.visit_expr_get_field" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#252-254"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_get_field"
class="fn">visit_expr_get_field</a>(&mut self, i: &'ast <a href="../struct.ExprGetField.html" class="struct"
title="struct verus_syn::ExprGetField">ExprGetField</a>)

</div>

<div id="method.visit_expr_group" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#257-259"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_group" class="fn">visit_expr_group</a>(&mut self, i: &'ast <a href="../struct.ExprGroup.html" class="struct"
title="struct verus_syn::ExprGroup">ExprGroup</a>)

</div>

<div id="method.visit_expr_has" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#260-262"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_has" class="fn">visit_expr_has</a>(&mut self, i: &'ast <a href="../struct.ExprHas.html" class="struct"
title="struct verus_syn::ExprHas">ExprHas</a>)

</div>

<div id="method.visit_expr_has_not" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#263-265"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_has_not" class="fn">visit_expr_has_not</a>(&mut self, i: &'ast <a href="../struct.ExprHasNot.html" class="struct"
title="struct verus_syn::ExprHasNot">ExprHasNot</a>)

</div>

<div id="method.visit_expr_if" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#268-270"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_if" class="fn">visit_expr_if</a>(&mut self, i: &'ast <a href="../struct.ExprIf.html" class="struct"
title="struct verus_syn::ExprIf">ExprIf</a>)

</div>

<div id="method.visit_expr_index" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#273-275"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_index" class="fn">visit_expr_index</a>(&mut self, i: &'ast <a href="../struct.ExprIndex.html" class="struct"
title="struct verus_syn::ExprIndex">ExprIndex</a>)

</div>

<div id="method.visit_expr_infer" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#278-280"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_infer" class="fn">visit_expr_infer</a>(&mut self, i: &'ast <a href="../struct.ExprInfer.html" class="struct"
title="struct verus_syn::ExprInfer">ExprInfer</a>)

</div>

<div id="method.visit_expr_is" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#281-283"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_is" class="fn">visit_expr_is</a>(&mut self, i: &'ast <a href="../struct.ExprIs.html" class="struct"
title="struct verus_syn::ExprIs">ExprIs</a>)

</div>

<div id="method.visit_expr_is_not" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#284-286"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_is_not" class="fn">visit_expr_is_not</a>(&mut self, i: &'ast <a href="../struct.ExprIsNot.html" class="struct"
title="struct verus_syn::ExprIsNot">ExprIsNot</a>)

</div>

<div id="method.visit_expr_let" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#289-291"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_let" class="fn">visit_expr_let</a>(&mut self, i: &'ast <a href="../struct.ExprLet.html" class="struct"
title="struct verus_syn::ExprLet">ExprLet</a>)

</div>

<div id="method.visit_expr_lit" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#294-296"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_lit" class="fn">visit_expr_lit</a>(&mut self, i: &'ast <a href="../struct.ExprLit.html" class="struct"
title="struct verus_syn::ExprLit">ExprLit</a>)

</div>

<div id="method.visit_expr_loop" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#299-301"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_loop" class="fn">visit_expr_loop</a>(&mut self, i: &'ast <a href="../struct.ExprLoop.html" class="struct"
title="struct verus_syn::ExprLoop">ExprLoop</a>)

</div>

<div id="method.visit_expr_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#304-306"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_macro" class="fn">visit_expr_macro</a>(&mut self, i: &'ast <a href="../struct.ExprMacro.html" class="struct"
title="struct verus_syn::ExprMacro">ExprMacro</a>)

</div>

<div id="method.visit_expr_match" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#309-311"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_match" class="fn">visit_expr_match</a>(&mut self, i: &'ast <a href="../struct.ExprMatch.html" class="struct"
title="struct verus_syn::ExprMatch">ExprMatch</a>)

</div>

<div id="method.visit_expr_matches" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#312-314"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_matches" class="fn">visit_expr_matches</a>(&mut self, i: &'ast <a href="../struct.ExprMatches.html" class="struct"
title="struct verus_syn::ExprMatches">ExprMatches</a>)

</div>

<div id="method.visit_expr_method_call" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#317-319"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_method_call"
class="fn">visit_expr_method_call</a>(&mut self, i: &'ast <a href="../struct.ExprMethodCall.html" class="struct"
title="struct verus_syn::ExprMethodCall">ExprMethodCall</a>)

</div>

<div id="method.visit_expr_paren" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#322-324"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_paren" class="fn">visit_expr_paren</a>(&mut self, i: &'ast <a href="../struct.ExprParen.html" class="struct"
title="struct verus_syn::ExprParen">ExprParen</a>)

</div>

<div id="method.visit_expr_path" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#327-329"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_path" class="fn">visit_expr_path</a>(&mut self, i: &'ast <a href="../struct.ExprPath.html" class="struct"
title="struct verus_syn::ExprPath">ExprPath</a>)

</div>

<div id="method.visit_expr_range" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#332-334"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_range" class="fn">visit_expr_range</a>(&mut self, i: &'ast <a href="../struct.ExprRange.html" class="struct"
title="struct verus_syn::ExprRange">ExprRange</a>)

</div>

<div id="method.visit_expr_raw_addr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#337-339"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_raw_addr" class="fn">visit_expr_raw_addr</a>(&mut self, i: &'ast <a href="../struct.ExprRawAddr.html" class="struct"
title="struct verus_syn::ExprRawAddr">ExprRawAddr</a>)

</div>

<div id="method.visit_expr_reference" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#342-344"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_reference"
class="fn">visit_expr_reference</a>(&mut self, i: &'ast <a href="../struct.ExprReference.html" class="struct"
title="struct verus_syn::ExprReference">ExprReference</a>)

</div>

<div id="method.visit_expr_repeat" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#347-349"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_repeat" class="fn">visit_expr_repeat</a>(&mut self, i: &'ast <a href="../struct.ExprRepeat.html" class="struct"
title="struct verus_syn::ExprRepeat">ExprRepeat</a>)

</div>

<div id="method.visit_expr_return" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#352-354"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_return" class="fn">visit_expr_return</a>(&mut self, i: &'ast <a href="../struct.ExprReturn.html" class="struct"
title="struct verus_syn::ExprReturn">ExprReturn</a>)

</div>

<div id="method.visit_expr_struct" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#357-359"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_struct" class="fn">visit_expr_struct</a>(&mut self, i: &'ast <a href="../struct.ExprStruct.html" class="struct"
title="struct verus_syn::ExprStruct">ExprStruct</a>)

</div>

<div id="method.visit_expr_try" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#362-364"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try" class="fn">visit_expr_try</a>(&mut self, i: &'ast <a href="../struct.ExprTry.html" class="struct"
title="struct verus_syn::ExprTry">ExprTry</a>)

</div>

<div id="method.visit_expr_try_block" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#367-369"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_block"
class="fn">visit_expr_try_block</a>(&mut self, i: &'ast <a href="../struct.ExprTryBlock.html" class="struct"
title="struct verus_syn::ExprTryBlock">ExprTryBlock</a>)

</div>

<div id="method.visit_expr_tuple" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#372-374"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_tuple" class="fn">visit_expr_tuple</a>(&mut self, i: &'ast <a href="../struct.ExprTuple.html" class="struct"
title="struct verus_syn::ExprTuple">ExprTuple</a>)

</div>

<div id="method.visit_expr_unary" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#377-379"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unary" class="fn">visit_expr_unary</a>(&mut self, i: &'ast <a href="../struct.ExprUnary.html" class="struct"
title="struct verus_syn::ExprUnary">ExprUnary</a>)

</div>

<div id="method.visit_expr_unsafe" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#382-384"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unsafe" class="fn">visit_expr_unsafe</a>(&mut self, i: &'ast <a href="../struct.ExprUnsafe.html" class="struct"
title="struct verus_syn::ExprUnsafe">ExprUnsafe</a>)

</div>

<div id="method.visit_expr_while" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#387-389"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_while" class="fn">visit_expr_while</a>(&mut self, i: &'ast <a href="../struct.ExprWhile.html" class="struct"
title="struct verus_syn::ExprWhile">ExprWhile</a>)

</div>

<div id="method.visit_expr_yield" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#392-394"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_yield" class="fn">visit_expr_yield</a>(&mut self, i: &'ast <a href="../struct.ExprYield.html" class="struct"
title="struct verus_syn::ExprYield">ExprYield</a>)

</div>

<div id="method.visit_field" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#397-399"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field" class="fn">visit_field</a>(&mut self, i: &'ast <a href="../struct.Field.html" class="struct"
title="struct verus_syn::Field">Field</a>)

</div>

<div id="method.visit_field_mutability" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#402-404"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mutability"
class="fn">visit_field_mutability</a>(&mut self, i: &'ast <a href="../enum.FieldMutability.html" class="enum"
title="enum verus_syn::FieldMutability">FieldMutability</a>)

</div>

<div id="method.visit_field_pat" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#407-409"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_pat" class="fn">visit_field_pat</a>(&mut self, i: &'ast <a href="../struct.FieldPat.html" class="struct"
title="struct verus_syn::FieldPat">FieldPat</a>)

</div>

<div id="method.visit_field_value" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#412-414"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_value" class="fn">visit_field_value</a>(&mut self, i: &'ast <a href="../struct.FieldValue.html" class="struct"
title="struct verus_syn::FieldValue">FieldValue</a>)

</div>

<div id="method.visit_fields" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#417-419"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields" class="fn">visit_fields</a>(&mut self, i: &'ast <a href="../enum.Fields.html" class="enum"
title="enum verus_syn::Fields">Fields</a>)

</div>

<div id="method.visit_fields_named" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#422-424"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_named" class="fn">visit_fields_named</a>(&mut self, i: &'ast <a href="../struct.FieldsNamed.html" class="struct"
title="struct verus_syn::FieldsNamed">FieldsNamed</a>)

</div>

<div id="method.visit_fields_unnamed" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#427-429"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_unnamed"
class="fn">visit_fields_unnamed</a>(&mut self, i: &'ast <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct verus_syn::FieldsUnnamed">FieldsUnnamed</a>)

</div>

<div id="method.visit_file" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#432-434"
class="src rightside">Source</a>

#### fn <a href="#method.visit_file" class="fn">visit_file</a>(&mut self, i: &'ast <a href="../struct.File.html" class="struct"
title="struct verus_syn::File">File</a>)

</div>

<div id="method.visit_fn_arg" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#437-439"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg" class="fn">visit_fn_arg</a>(&mut self, i: &'ast <a href="../struct.FnArg.html" class="struct"
title="struct verus_syn::FnArg">FnArg</a>)

</div>

<div id="method.visit_fn_arg_kind" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#442-444"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg_kind" class="fn">visit_fn_arg_kind</a>(&mut self, i: &'ast <a href="../enum.FnArgKind.html" class="enum"
title="enum verus_syn::FnArgKind">FnArgKind</a>)

</div>

<div id="method.visit_fn_mode" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#445-447"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_mode" class="fn">visit_fn_mode</a>(&mut self, i: &'ast <a href="../enum.FnMode.html" class="enum"
title="enum verus_syn::FnMode">FnMode</a>)

</div>

<div id="method.visit_fn_proof_arg" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#448-450"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_proof_arg" class="fn">visit_fn_proof_arg</a>(&mut self, i: &'ast <a href="../struct.FnProofArg.html" class="struct"
title="struct verus_syn::FnProofArg">FnProofArg</a>)

</div>

<div id="method.visit_fn_proof_options" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#451-453"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_proof_options"
class="fn">visit_fn_proof_options</a>(&mut self, i: &'ast <a href="../struct.FnProofOptions.html" class="struct"
title="struct verus_syn::FnProofOptions">FnProofOptions</a>)

</div>

<div id="method.visit_foreign_item" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#456-458"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item" class="fn">visit_foreign_item</a>(&mut self, i: &'ast <a href="../enum.ForeignItem.html" class="enum"
title="enum verus_syn::ForeignItem">ForeignItem</a>)

</div>

<div id="method.visit_foreign_item_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#461-463"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_fn"
class="fn">visit_foreign_item_fn</a>(&mut self, i: &'ast <a href="../struct.ForeignItemFn.html" class="struct"
title="struct verus_syn::ForeignItemFn">ForeignItemFn</a>)

</div>

<div id="method.visit_foreign_item_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#466-468"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_macro"
class="fn">visit_foreign_item_macro</a>(&mut self, i: &'ast <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct verus_syn::ForeignItemMacro">ForeignItemMacro</a>)

</div>

<div id="method.visit_foreign_item_static" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#471-473"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_static"
class="fn">visit_foreign_item_static</a>(&mut self, i: &'ast <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct verus_syn::ForeignItemStatic">ForeignItemStatic</a>)

</div>

<div id="method.visit_foreign_item_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#476-478"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_type"
class="fn">visit_foreign_item_type</a>(&mut self, i: &'ast <a href="../struct.ForeignItemType.html" class="struct"
title="struct verus_syn::ForeignItemType">ForeignItemType</a>)

</div>

<div id="method.visit_generic_argument" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#481-483"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_argument"
class="fn">visit_generic_argument</a>(&mut self, i: &'ast <a href="../enum.GenericArgument.html" class="enum"
title="enum verus_syn::GenericArgument">GenericArgument</a>)

</div>

<div id="method.visit_generic_param" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#486-488"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_param" class="fn">visit_generic_param</a>(&mut self, i: &'ast <a href="../enum.GenericParam.html" class="enum"
title="enum verus_syn::GenericParam">GenericParam</a>)

</div>

<div id="method.visit_generics" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#491-493"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generics" class="fn">visit_generics</a>(&mut self, i: &'ast <a href="../struct.Generics.html" class="struct"
title="struct verus_syn::Generics">Generics</a>)

</div>

<div id="method.visit_global" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#494-496"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global" class="fn">visit_global</a>(&mut self, i: &'ast <a href="../struct.Global.html" class="struct"
title="struct verus_syn::Global">Global</a>)

</div>

<div id="method.visit_global_inner" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#497-499"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_inner" class="fn">visit_global_inner</a>(&mut self, i: &'ast <a href="../enum.GlobalInner.html" class="enum"
title="enum verus_syn::GlobalInner">GlobalInner</a>)

</div>

<div id="method.visit_global_layout" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#500-502"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_layout" class="fn">visit_global_layout</a>(&mut self, i: &'ast <a href="../struct.GlobalLayout.html" class="struct"
title="struct verus_syn::GlobalLayout">GlobalLayout</a>)

</div>

<div id="method.visit_global_size_of" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#503-505"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_size_of"
class="fn">visit_global_size_of</a>(&mut self, i: &'ast <a href="../struct.GlobalSizeOf.html" class="struct"
title="struct verus_syn::GlobalSizeOf">GlobalSizeOf</a>)

</div>

<div id="method.visit_ident" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#506-508"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ident" class="fn">visit_ident</a>(&mut self, i: &'ast <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>)

</div>

<div id="method.visit_impl_item" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#511-513"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item" class="fn">visit_impl_item</a>(&mut self, i: &'ast <a href="../enum.ImplItem.html" class="enum"
title="enum verus_syn::ImplItem">ImplItem</a>)

</div>

<div id="method.visit_impl_item_const" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#516-518"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_const"
class="fn">visit_impl_item_const</a>(&mut self, i: &'ast <a href="../struct.ImplItemConst.html" class="struct"
title="struct verus_syn::ImplItemConst">ImplItemConst</a>)

</div>

<div id="method.visit_impl_item_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#521-523"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_fn" class="fn">visit_impl_item_fn</a>(&mut self, i: &'ast <a href="../struct.ImplItemFn.html" class="struct"
title="struct verus_syn::ImplItemFn">ImplItemFn</a>)

</div>

<div id="method.visit_impl_item_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#526-528"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_macro"
class="fn">visit_impl_item_macro</a>(&mut self, i: &'ast <a href="../struct.ImplItemMacro.html" class="struct"
title="struct verus_syn::ImplItemMacro">ImplItemMacro</a>)

</div>

<div id="method.visit_impl_item_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#531-533"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_type"
class="fn">visit_impl_item_type</a>(&mut self, i: &'ast <a href="../struct.ImplItemType.html" class="struct"
title="struct verus_syn::ImplItemType">ImplItemType</a>)

</div>

<div id="method.visit_impl_restriction" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#536-538"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_restriction"
class="fn">visit_impl_restriction</a>(&mut self, i: &'ast <a href="../enum.ImplRestriction.html" class="enum"
title="enum verus_syn::ImplRestriction">ImplRestriction</a>)

</div>

<div id="method.visit_index" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#541-543"
class="src rightside">Source</a>

#### fn <a href="#method.visit_index" class="fn">visit_index</a>(&mut self, i: &'ast <a href="../struct.Index.html" class="struct"
title="struct verus_syn::Index">Index</a>)

</div>

<div id="method.visit_invariant" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#544-546"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant" class="fn">visit_invariant</a>(&mut self, i: &'ast <a href="../struct.Invariant.html" class="struct"
title="struct verus_syn::Invariant">Invariant</a>)

</div>

<div id="method.visit_invariant_ensures" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#547-549"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_ensures"
class="fn">visit_invariant_ensures</a>(&mut self, i: &'ast <a href="../struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::InvariantEnsures">InvariantEnsures</a>)

</div>

<div id="method.visit_invariant_except_break" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#550-552"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_except_break"
class="fn">visit_invariant_except_break</a>(&mut self, i: &'ast <a href="../struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::InvariantExceptBreak">InvariantExceptBreak</a>)

</div>

<div id="method.visit_invariant_name_set" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#553-555"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set"
class="fn">visit_invariant_name_set</a>(&mut self, i: &'ast <a href="../enum.InvariantNameSet.html" class="enum"
title="enum verus_syn::InvariantNameSet">InvariantNameSet</a>)

</div>

<div id="method.visit_invariant_name_set_any" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#556-558"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_any"
class="fn">visit_invariant_name_set_any</a>(&mut self, i: &'ast <a href="../struct.InvariantNameSetAny.html" class="struct"
title="struct verus_syn::InvariantNameSetAny">InvariantNameSetAny</a>)

</div>

<div id="method.visit_invariant_name_set_list" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#559-561"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_list"
class="fn">visit_invariant_name_set_list</a>(&mut self, i: &'ast <a href="../struct.InvariantNameSetList.html" class="struct"
title="struct verus_syn::InvariantNameSetList">InvariantNameSetList</a>)

</div>

<div id="method.visit_invariant_name_set_none" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#562-564"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_none"
class="fn">visit_invariant_name_set_none</a>(&mut self, i: &'ast <a href="../struct.InvariantNameSetNone.html" class="struct"
title="struct verus_syn::InvariantNameSetNone">InvariantNameSetNone</a>)

</div>

<div id="method.visit_invariant_name_set_set" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#565-567"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_set"
class="fn">visit_invariant_name_set_set</a>(&mut self, i: &'ast <a href="../struct.InvariantNameSetSet.html" class="struct"
title="struct verus_syn::InvariantNameSetSet">InvariantNameSetSet</a>)

</div>

<div id="method.visit_item" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#570-572"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item" class="fn">visit_item</a>(&mut self, i: &'ast <a href="../enum.Item.html" class="enum"
title="enum verus_syn::Item">Item</a>)

</div>

<div id="method.visit_item_broadcast_group" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#573-575"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_broadcast_group"
class="fn">visit_item_broadcast_group</a>(&mut self, i: &'ast <a href="../struct.ItemBroadcastGroup.html" class="struct"
title="struct verus_syn::ItemBroadcastGroup">ItemBroadcastGroup</a>)

</div>

<div id="method.visit_item_const" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#578-580"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_const" class="fn">visit_item_const</a>(&mut self, i: &'ast <a href="../struct.ItemConst.html" class="struct"
title="struct verus_syn::ItemConst">ItemConst</a>)

</div>

<div id="method.visit_item_enum" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#583-585"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_enum" class="fn">visit_item_enum</a>(&mut self, i: &'ast <a href="../struct.ItemEnum.html" class="struct"
title="struct verus_syn::ItemEnum">ItemEnum</a>)

</div>

<div id="method.visit_item_extern_crate" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#588-590"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_extern_crate"
class="fn">visit_item_extern_crate</a>(&mut self, i: &'ast <a href="../struct.ItemExternCrate.html" class="struct"
title="struct verus_syn::ItemExternCrate">ItemExternCrate</a>)

</div>

<div id="method.visit_item_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#593-595"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_fn" class="fn">visit_item_fn</a>(&mut self, i: &'ast <a href="../struct.ItemFn.html" class="struct"
title="struct verus_syn::ItemFn">ItemFn</a>)

</div>

<div id="method.visit_item_foreign_mod" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#598-600"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_foreign_mod"
class="fn">visit_item_foreign_mod</a>(&mut self, i: &'ast <a href="../struct.ItemForeignMod.html" class="struct"
title="struct verus_syn::ItemForeignMod">ItemForeignMod</a>)

</div>

<div id="method.visit_item_impl" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#603-605"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_impl" class="fn">visit_item_impl</a>(&mut self, i: &'ast <a href="../struct.ItemImpl.html" class="struct"
title="struct verus_syn::ItemImpl">ItemImpl</a>)

</div>

<div id="method.visit_item_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#608-610"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_macro" class="fn">visit_item_macro</a>(&mut self, i: &'ast <a href="../struct.ItemMacro.html" class="struct"
title="struct verus_syn::ItemMacro">ItemMacro</a>)

</div>

<div id="method.visit_item_mod" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#613-615"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mod" class="fn">visit_item_mod</a>(&mut self, i: &'ast <a href="../struct.ItemMod.html" class="struct"
title="struct verus_syn::ItemMod">ItemMod</a>)

</div>

<div id="method.visit_item_static" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#618-620"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_static" class="fn">visit_item_static</a>(&mut self, i: &'ast <a href="../struct.ItemStatic.html" class="struct"
title="struct verus_syn::ItemStatic">ItemStatic</a>)

</div>

<div id="method.visit_item_struct" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#623-625"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_struct" class="fn">visit_item_struct</a>(&mut self, i: &'ast <a href="../struct.ItemStruct.html" class="struct"
title="struct verus_syn::ItemStruct">ItemStruct</a>)

</div>

<div id="method.visit_item_trait" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#628-630"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait" class="fn">visit_item_trait</a>(&mut self, i: &'ast <a href="../struct.ItemTrait.html" class="struct"
title="struct verus_syn::ItemTrait">ItemTrait</a>)

</div>

<div id="method.visit_item_trait_alias" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#633-635"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_alias"
class="fn">visit_item_trait_alias</a>(&mut self, i: &'ast <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct verus_syn::ItemTraitAlias">ItemTraitAlias</a>)

</div>

<div id="method.visit_item_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#638-640"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_type" class="fn">visit_item_type</a>(&mut self, i: &'ast <a href="../struct.ItemType.html" class="struct"
title="struct verus_syn::ItemType">ItemType</a>)

</div>

<div id="method.visit_item_union" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#643-645"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_union" class="fn">visit_item_union</a>(&mut self, i: &'ast <a href="../struct.ItemUnion.html" class="struct"
title="struct verus_syn::ItemUnion">ItemUnion</a>)

</div>

<div id="method.visit_item_use" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#648-650"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_use" class="fn">visit_item_use</a>(&mut self, i: &'ast <a href="../struct.ItemUse.html" class="struct"
title="struct verus_syn::ItemUse">ItemUse</a>)

</div>

<div id="method.visit_label" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#653-655"
class="src rightside">Source</a>

#### fn <a href="#method.visit_label" class="fn">visit_label</a>(&mut self, i: &'ast <a href="../struct.Label.html" class="struct"
title="struct verus_syn::Label">Label</a>)

</div>

<div id="method.visit_lifetime" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#656-658"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime" class="fn">visit_lifetime</a>(&mut self, i: &'ast <a href="../struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>)

</div>

<div id="method.visit_lifetime_param" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#661-663"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_param"
class="fn">visit_lifetime_param</a>(&mut self, i: &'ast <a href="../struct.LifetimeParam.html" class="struct"
title="struct verus_syn::LifetimeParam">LifetimeParam</a>)

</div>

<div id="method.visit_lit" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#664-666"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit" class="fn">visit_lit</a>(&mut self, i: &'ast <a href="../enum.Lit.html" class="enum"
title="enum verus_syn::Lit">Lit</a>)

</div>

<div id="method.visit_lit_bool" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#667-669"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_bool" class="fn">visit_lit_bool</a>(&mut self, i: &'ast <a href="../struct.LitBool.html" class="struct"
title="struct verus_syn::LitBool">LitBool</a>)

</div>

<div id="method.visit_lit_byte" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#670-672"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte" class="fn">visit_lit_byte</a>(&mut self, i: &'ast <a href="../struct.LitByte.html" class="struct"
title="struct verus_syn::LitByte">LitByte</a>)

</div>

<div id="method.visit_lit_byte_str" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#673-675"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_str" class="fn">visit_lit_byte_str</a>(&mut self, i: &'ast <a href="../struct.LitByteStr.html" class="struct"
title="struct verus_syn::LitByteStr">LitByteStr</a>)

</div>

<div id="method.visit_lit_cstr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#676-678"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_cstr" class="fn">visit_lit_cstr</a>(&mut self, i: &'ast <a href="../struct.LitCStr.html" class="struct"
title="struct verus_syn::LitCStr">LitCStr</a>)

</div>

<div id="method.visit_lit_char" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#679-681"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_char" class="fn">visit_lit_char</a>(&mut self, i: &'ast <a href="../struct.LitChar.html" class="struct"
title="struct verus_syn::LitChar">LitChar</a>)

</div>

<div id="method.visit_lit_float" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#682-684"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_float" class="fn">visit_lit_float</a>(&mut self, i: &'ast <a href="../struct.LitFloat.html" class="struct"
title="struct verus_syn::LitFloat">LitFloat</a>)

</div>

<div id="method.visit_lit_int" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#685-687"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_int" class="fn">visit_lit_int</a>(&mut self, i: &'ast <a href="../struct.LitInt.html" class="struct"
title="struct verus_syn::LitInt">LitInt</a>)

</div>

<div id="method.visit_lit_str" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#688-690"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_str" class="fn">visit_lit_str</a>(&mut self, i: &'ast <a href="../struct.LitStr.html" class="struct"
title="struct verus_syn::LitStr">LitStr</a>)

</div>

<div id="method.visit_local" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#693-695"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local" class="fn">visit_local</a>(&mut self, i: &'ast <a href="../struct.Local.html" class="struct"
title="struct verus_syn::Local">Local</a>)

</div>

<div id="method.visit_local_init" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#698-700"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_init" class="fn">visit_local_init</a>(&mut self, i: &'ast <a href="../struct.LocalInit.html" class="struct"
title="struct verus_syn::LocalInit">LocalInit</a>)

</div>

<div id="method.visit_loop_spec" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#701-703"
class="src rightside">Source</a>

#### fn <a href="#method.visit_loop_spec" class="fn">visit_loop_spec</a>(&mut self, i: &'ast <a href="../struct.LoopSpec.html" class="struct"
title="struct verus_syn::LoopSpec">LoopSpec</a>)

</div>

<div id="method.visit_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#706-708"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro" class="fn">visit_macro</a>(&mut self, i: &'ast <a href="../struct.Macro.html" class="struct"
title="struct verus_syn::Macro">Macro</a>)

</div>

<div id="method.visit_macro_delimiter" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#711-713"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_delimiter"
class="fn">visit_macro_delimiter</a>(&mut self, i: &'ast <a href="../enum.MacroDelimiter.html" class="enum"
title="enum verus_syn::MacroDelimiter">MacroDelimiter</a>)

</div>

<div id="method.visit_matches_op_expr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#714-716"
class="src rightside">Source</a>

#### fn <a href="#method.visit_matches_op_expr"
class="fn">visit_matches_op_expr</a>(&mut self, i: &'ast <a href="../struct.MatchesOpExpr.html" class="struct"
title="struct verus_syn::MatchesOpExpr">MatchesOpExpr</a>)

</div>

<div id="method.visit_matches_op_token" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#717-719"
class="src rightside">Source</a>

#### fn <a href="#method.visit_matches_op_token"
class="fn">visit_matches_op_token</a>(&mut self, i: &'ast <a href="../enum.MatchesOpToken.html" class="enum"
title="enum verus_syn::MatchesOpToken">MatchesOpToken</a>)

</div>

<div id="method.visit_member" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#722-724"
class="src rightside">Source</a>

#### fn <a href="#method.visit_member" class="fn">visit_member</a>(&mut self, i: &'ast <a href="../enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>)

</div>

<div id="method.visit_meta" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#727-729"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta" class="fn">visit_meta</a>(&mut self, i: &'ast <a href="../enum.Meta.html" class="enum"
title="enum verus_syn::Meta">Meta</a>)

</div>

<div id="method.visit_meta_list" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#732-734"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_list" class="fn">visit_meta_list</a>(&mut self, i: &'ast <a href="../struct.MetaList.html" class="struct"
title="struct verus_syn::MetaList">MetaList</a>)

</div>

<div id="method.visit_meta_name_value" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#737-739"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_name_value"
class="fn">visit_meta_name_value</a>(&mut self, i: &'ast <a href="../struct.MetaNameValue.html" class="struct"
title="struct verus_syn::MetaNameValue">MetaNameValue</a>)

</div>

<div id="method.visit_mode" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#740-742"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode" class="fn">visit_mode</a>(&mut self, i: &'ast <a href="../enum.Mode.html" class="enum"
title="enum verus_syn::Mode">Mode</a>)

</div>

<div id="method.visit_mode_exec" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#743-745"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_exec" class="fn">visit_mode_exec</a>(&mut self, i: &'ast <a href="../struct.ModeExec.html" class="struct"
title="struct verus_syn::ModeExec">ModeExec</a>)

</div>

<div id="method.visit_mode_ghost" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#746-748"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_ghost" class="fn">visit_mode_ghost</a>(&mut self, i: &'ast <a href="../struct.ModeGhost.html" class="struct"
title="struct verus_syn::ModeGhost">ModeGhost</a>)

</div>

<div id="method.visit_mode_proof" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#749-751"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_proof" class="fn">visit_mode_proof</a>(&mut self, i: &'ast <a href="../struct.ModeProof.html" class="struct"
title="struct verus_syn::ModeProof">ModeProof</a>)

</div>

<div id="method.visit_mode_proof_axiom" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#752-754"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_proof_axiom"
class="fn">visit_mode_proof_axiom</a>(&mut self, i: &'ast <a href="../struct.ModeProofAxiom.html" class="struct"
title="struct verus_syn::ModeProofAxiom">ModeProofAxiom</a>)

</div>

<div id="method.visit_mode_spec" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#755-757"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_spec" class="fn">visit_mode_spec</a>(&mut self, i: &'ast <a href="../struct.ModeSpec.html" class="struct"
title="struct verus_syn::ModeSpec">ModeSpec</a>)

</div>

<div id="method.visit_mode_spec_checked" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#758-760"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_spec_checked"
class="fn">visit_mode_spec_checked</a>(&mut self, i: &'ast <a href="../struct.ModeSpecChecked.html" class="struct"
title="struct verus_syn::ModeSpecChecked">ModeSpecChecked</a>)

</div>

<div id="method.visit_mode_tracked" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#761-763"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_tracked" class="fn">visit_mode_tracked</a>(&mut self, i: &'ast <a href="../struct.ModeTracked.html" class="struct"
title="struct verus_syn::ModeTracked">ModeTracked</a>)

</div>

<div id="method.visit_open" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#764-766"
class="src rightside">Source</a>

#### fn <a href="#method.visit_open" class="fn">visit_open</a>(&mut self, i: &'ast <a href="../struct.Open.html" class="struct"
title="struct verus_syn::Open">Open</a>)

</div>

<div id="method.visit_open_restricted" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#767-769"
class="src rightside">Source</a>

#### fn <a href="#method.visit_open_restricted"
class="fn">visit_open_restricted</a>(&mut self, i: &'ast <a href="../struct.OpenRestricted.html" class="struct"
title="struct verus_syn::OpenRestricted">OpenRestricted</a>)

</div>

<div id="method.visit_parenthesized_generic_arguments"
class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#772-777"
class="src rightside">Source</a>

#### fn <a href="#method.visit_parenthesized_generic_arguments"
class="fn">visit_parenthesized_generic_arguments</a>( &mut self, i: &'ast <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct verus_syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>, )

</div>

<div id="method.visit_pat" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#780-782"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat" class="fn">visit_pat</a>(&mut self, i: &'ast <a href="../enum.Pat.html" class="enum"
title="enum verus_syn::Pat">Pat</a>)

</div>

<div id="method.visit_pat_ident" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#785-787"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_ident" class="fn">visit_pat_ident</a>(&mut self, i: &'ast <a href="../struct.PatIdent.html" class="struct"
title="struct verus_syn::PatIdent">PatIdent</a>)

</div>

<div id="method.visit_pat_or" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#790-792"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_or" class="fn">visit_pat_or</a>(&mut self, i: &'ast <a href="../struct.PatOr.html" class="struct"
title="struct verus_syn::PatOr">PatOr</a>)

</div>

<div id="method.visit_pat_paren" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#795-797"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_paren" class="fn">visit_pat_paren</a>(&mut self, i: &'ast <a href="../struct.PatParen.html" class="struct"
title="struct verus_syn::PatParen">PatParen</a>)

</div>

<div id="method.visit_pat_reference" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#800-802"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_reference" class="fn">visit_pat_reference</a>(&mut self, i: &'ast <a href="../struct.PatReference.html" class="struct"
title="struct verus_syn::PatReference">PatReference</a>)

</div>

<div id="method.visit_pat_rest" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#805-807"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_rest" class="fn">visit_pat_rest</a>(&mut self, i: &'ast <a href="../struct.PatRest.html" class="struct"
title="struct verus_syn::PatRest">PatRest</a>)

</div>

<div id="method.visit_pat_slice" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#810-812"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_slice" class="fn">visit_pat_slice</a>(&mut self, i: &'ast <a href="../struct.PatSlice.html" class="struct"
title="struct verus_syn::PatSlice">PatSlice</a>)

</div>

<div id="method.visit_pat_struct" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#815-817"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_struct" class="fn">visit_pat_struct</a>(&mut self, i: &'ast <a href="../struct.PatStruct.html" class="struct"
title="struct verus_syn::PatStruct">PatStruct</a>)

</div>

<div id="method.visit_pat_tuple" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#820-822"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple" class="fn">visit_pat_tuple</a>(&mut self, i: &'ast <a href="../struct.PatTuple.html" class="struct"
title="struct verus_syn::PatTuple">PatTuple</a>)

</div>

<div id="method.visit_pat_tuple_struct" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#825-827"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_struct"
class="fn">visit_pat_tuple_struct</a>(&mut self, i: &'ast <a href="../struct.PatTupleStruct.html" class="struct"
title="struct verus_syn::PatTupleStruct">PatTupleStruct</a>)

</div>

<div id="method.visit_pat_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#830-832"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_type" class="fn">visit_pat_type</a>(&mut self, i: &'ast <a href="../struct.PatType.html" class="struct"
title="struct verus_syn::PatType">PatType</a>)

</div>

<div id="method.visit_pat_wild" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#835-837"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_wild" class="fn">visit_pat_wild</a>(&mut self, i: &'ast <a href="../struct.PatWild.html" class="struct"
title="struct verus_syn::PatWild">PatWild</a>)

</div>

<div id="method.visit_path" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#840-842"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path" class="fn">visit_path</a>(&mut self, i: &'ast <a href="../struct.Path.html" class="struct"
title="struct verus_syn::Path">Path</a>)

</div>

<div id="method.visit_path_arguments" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#845-847"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_arguments"
class="fn">visit_path_arguments</a>(&mut self, i: &'ast <a href="../enum.PathArguments.html" class="enum"
title="enum verus_syn::PathArguments">PathArguments</a>)

</div>

<div id="method.visit_path_segment" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#850-852"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_segment" class="fn">visit_path_segment</a>(&mut self, i: &'ast <a href="../struct.PathSegment.html" class="struct"
title="struct verus_syn::PathSegment">PathSegment</a>)

</div>

<div id="method.visit_pointer_mutability" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#855-857"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pointer_mutability"
class="fn">visit_pointer_mutability</a>(&mut self, i: &'ast <a href="../enum.PointerMutability.html" class="enum"
title="enum verus_syn::PointerMutability">PointerMutability</a>)

</div>

<div id="method.visit_precise_capture" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#860-862"
class="src rightside">Source</a>

#### fn <a href="#method.visit_precise_capture"
class="fn">visit_precise_capture</a>(&mut self, i: &'ast <a href="../struct.PreciseCapture.html" class="struct"
title="struct verus_syn::PreciseCapture">PreciseCapture</a>)

</div>

<div id="method.visit_predicate_lifetime" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#865-867"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_lifetime"
class="fn">visit_predicate_lifetime</a>(&mut self, i: &'ast <a href="../struct.PredicateLifetime.html" class="struct"
title="struct verus_syn::PredicateLifetime">PredicateLifetime</a>)

</div>

<div id="method.visit_predicate_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#870-872"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_type"
class="fn">visit_predicate_type</a>(&mut self, i: &'ast <a href="../struct.PredicateType.html" class="struct"
title="struct verus_syn::PredicateType">PredicateType</a>)

</div>

<div id="method.visit_prover" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#873-875"
class="src rightside">Source</a>

#### fn <a href="#method.visit_prover" class="fn">visit_prover</a>(&mut self, i: &'ast <a href="../struct.Prover.html" class="struct"
title="struct verus_syn::Prover">Prover</a>)

</div>

<div id="method.visit_publish" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#876-878"
class="src rightside">Source</a>

#### fn <a href="#method.visit_publish" class="fn">visit_publish</a>(&mut self, i: &'ast <a href="../enum.Publish.html" class="enum"
title="enum verus_syn::Publish">Publish</a>)

</div>

<div id="method.visit_qself" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#881-883"
class="src rightside">Source</a>

#### fn <a href="#method.visit_qself" class="fn">visit_qself</a>(&mut self, i: &'ast <a href="../struct.QSelf.html" class="struct"
title="struct verus_syn::QSelf">QSelf</a>)

</div>

<div id="method.visit_range_limits" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#886-888"
class="src rightside">Source</a>

#### fn <a href="#method.visit_range_limits" class="fn">visit_range_limits</a>(&mut self, i: &'ast <a href="../enum.RangeLimits.html" class="enum"
title="enum verus_syn::RangeLimits">RangeLimits</a>)

</div>

<div id="method.visit_receiver" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#891-893"
class="src rightside">Source</a>

#### fn <a href="#method.visit_receiver" class="fn">visit_receiver</a>(&mut self, i: &'ast <a href="../struct.Receiver.html" class="struct"
title="struct verus_syn::Receiver">Receiver</a>)

</div>

<div id="method.visit_recommends" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#894-896"
class="src rightside">Source</a>

#### fn <a href="#method.visit_recommends" class="fn">visit_recommends</a>(&mut self, i: &'ast <a href="../struct.Recommends.html" class="struct"
title="struct verus_syn::Recommends">Recommends</a>)

</div>

<div id="method.visit_requires" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#897-899"
class="src rightside">Source</a>

#### fn <a href="#method.visit_requires" class="fn">visit_requires</a>(&mut self, i: &'ast <a href="../struct.Requires.html" class="struct"
title="struct verus_syn::Requires">Requires</a>)

</div>

<div id="method.visit_return_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#902-904"
class="src rightside">Source</a>

#### fn <a href="#method.visit_return_type" class="fn">visit_return_type</a>(&mut self, i: &'ast <a href="../enum.ReturnType.html" class="enum"
title="enum verus_syn::ReturnType">ReturnType</a>)

</div>

<div id="method.visit_returns" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#905-907"
class="src rightside">Source</a>

#### fn <a href="#method.visit_returns" class="fn">visit_returns</a>(&mut self, i: &'ast <a href="../struct.Returns.html" class="struct"
title="struct verus_syn::Returns">Returns</a>)

</div>

<div id="method.visit_reveal_hide" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#908-910"
class="src rightside">Source</a>

#### fn <a href="#method.visit_reveal_hide" class="fn">visit_reveal_hide</a>(&mut self, i: &'ast <a href="../struct.RevealHide.html" class="struct"
title="struct verus_syn::RevealHide">RevealHide</a>)

</div>

<div id="method.visit_signature" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#913-915"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature" class="fn">visit_signature</a>(&mut self, i: &'ast <a href="../struct.Signature.html" class="struct"
title="struct verus_syn::Signature">Signature</a>)

</div>

<div id="method.visit_signature_decreases" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#916-918"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_decreases"
class="fn">visit_signature_decreases</a>(&mut self, i: &'ast <a href="../struct.SignatureDecreases.html" class="struct"
title="struct verus_syn::SignatureDecreases">SignatureDecreases</a>)

</div>

<div id="method.visit_signature_invariants" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#919-921"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_invariants"
class="fn">visit_signature_invariants</a>(&mut self, i: &'ast <a href="../struct.SignatureInvariants.html" class="struct"
title="struct verus_syn::SignatureInvariants">SignatureInvariants</a>)

</div>

<div id="method.visit_signature_spec" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#922-924"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_spec"
class="fn">visit_signature_spec</a>(&mut self, i: &'ast <a href="../struct.SignatureSpec.html" class="struct"
title="struct verus_syn::SignatureSpec">SignatureSpec</a>)

</div>

<div id="method.visit_signature_spec_attr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#925-927"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_spec_attr"
class="fn">visit_signature_spec_attr</a>(&mut self, i: &'ast <a href="../struct.SignatureSpecAttr.html" class="struct"
title="struct verus_syn::SignatureSpecAttr">SignatureSpecAttr</a>)

</div>

<div id="method.visit_signature_unwind" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#928-930"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_unwind"
class="fn">visit_signature_unwind</a>(&mut self, i: &'ast <a href="../struct.SignatureUnwind.html" class="struct"
title="struct verus_syn::SignatureUnwind">SignatureUnwind</a>)

</div>

<div id="method.visit_span" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#931"
class="src rightside">Source</a>

#### fn <a href="#method.visit_span" class="fn">visit_span</a>(&mut self, i: &<a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div id="method.visit_specification" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#932-934"
class="src rightside">Source</a>

#### fn <a href="#method.visit_specification" class="fn">visit_specification</a>(&mut self, i: &'ast <a href="../struct.Specification.html" class="struct"
title="struct verus_syn::Specification">Specification</a>)

</div>

<div id="method.visit_static_mutability" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#937-939"
class="src rightside">Source</a>

#### fn <a href="#method.visit_static_mutability"
class="fn">visit_static_mutability</a>(&mut self, i: &'ast <a href="../enum.StaticMutability.html" class="enum"
title="enum verus_syn::StaticMutability">StaticMutability</a>)

</div>

<div id="method.visit_stmt" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#942-944"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt" class="fn">visit_stmt</a>(&mut self, i: &'ast <a href="../enum.Stmt.html" class="enum"
title="enum verus_syn::Stmt">Stmt</a>)

</div>

<div id="method.visit_stmt_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#947-949"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_macro" class="fn">visit_stmt_macro</a>(&mut self, i: &'ast <a href="../struct.StmtMacro.html" class="struct"
title="struct verus_syn::StmtMacro">StmtMacro</a>)

</div>

<div id="method.visit_token_stream" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#950"
class="src rightside">Source</a>

#### fn <a href="#method.visit_token_stream" class="fn">visit_token_stream</a>(&mut self, i: &'ast <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div id="method.visit_trait_bound" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#953-955"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound" class="fn">visit_trait_bound</a>(&mut self, i: &'ast <a href="../struct.TraitBound.html" class="struct"
title="struct verus_syn::TraitBound">TraitBound</a>)

</div>

<div id="method.visit_trait_bound_modifier" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#958-960"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_modifier"
class="fn">visit_trait_bound_modifier</a>(&mut self, i: &'ast <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum verus_syn::TraitBoundModifier">TraitBoundModifier</a>)

</div>

<div id="method.visit_trait_item" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#963-965"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item" class="fn">visit_trait_item</a>(&mut self, i: &'ast <a href="../enum.TraitItem.html" class="enum"
title="enum verus_syn::TraitItem">TraitItem</a>)

</div>

<div id="method.visit_trait_item_const" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#968-970"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_const"
class="fn">visit_trait_item_const</a>(&mut self, i: &'ast <a href="../struct.TraitItemConst.html" class="struct"
title="struct verus_syn::TraitItemConst">TraitItemConst</a>)

</div>

<div id="method.visit_trait_item_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#973-975"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_fn" class="fn">visit_trait_item_fn</a>(&mut self, i: &'ast <a href="../struct.TraitItemFn.html" class="struct"
title="struct verus_syn::TraitItemFn">TraitItemFn</a>)

</div>

<div id="method.visit_trait_item_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#978-980"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_macro"
class="fn">visit_trait_item_macro</a>(&mut self, i: &'ast <a href="../struct.TraitItemMacro.html" class="struct"
title="struct verus_syn::TraitItemMacro">TraitItemMacro</a>)

</div>

<div id="method.visit_trait_item_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#983-985"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_type"
class="fn">visit_trait_item_type</a>(&mut self, i: &'ast <a href="../struct.TraitItemType.html" class="struct"
title="struct verus_syn::TraitItemType">TraitItemType</a>)

</div>

<div id="method.visit_type" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#988-990"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type" class="fn">visit_type</a>(&mut self, i: &'ast <a href="../enum.Type.html" class="enum"
title="enum verus_syn::Type">Type</a>)

</div>

<div id="method.visit_type_array" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#993-995"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_array" class="fn">visit_type_array</a>(&mut self, i: &'ast <a href="../struct.TypeArray.html" class="struct"
title="struct verus_syn::TypeArray">TypeArray</a>)

</div>

<div id="method.visit_type_bare_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#998-1000"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_bare_fn" class="fn">visit_type_bare_fn</a>(&mut self, i: &'ast <a href="../struct.TypeBareFn.html" class="struct"
title="struct verus_syn::TypeBareFn">TypeBareFn</a>)

</div>

<div id="method.visit_type_fn_proof" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1001-1003"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_fn_proof" class="fn">visit_type_fn_proof</a>(&mut self, i: &'ast <a href="../struct.TypeFnProof.html" class="struct"
title="struct verus_syn::TypeFnProof">TypeFnProof</a>)

</div>

<div id="method.visit_type_fn_spec" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1004-1006"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_fn_spec" class="fn">visit_type_fn_spec</a>(&mut self, i: &'ast <a href="../struct.TypeFnSpec.html" class="struct"
title="struct verus_syn::TypeFnSpec">TypeFnSpec</a>)

</div>

<div id="method.visit_type_group" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1009-1011"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_group" class="fn">visit_type_group</a>(&mut self, i: &'ast <a href="../struct.TypeGroup.html" class="struct"
title="struct verus_syn::TypeGroup">TypeGroup</a>)

</div>

<div id="method.visit_type_impl_trait" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1014-1016"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_impl_trait"
class="fn">visit_type_impl_trait</a>(&mut self, i: &'ast <a href="../struct.TypeImplTrait.html" class="struct"
title="struct verus_syn::TypeImplTrait">TypeImplTrait</a>)

</div>

<div id="method.visit_type_infer" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1019-1021"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_infer" class="fn">visit_type_infer</a>(&mut self, i: &'ast <a href="../struct.TypeInfer.html" class="struct"
title="struct verus_syn::TypeInfer">TypeInfer</a>)

</div>

<div id="method.visit_type_macro" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1024-1026"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_macro" class="fn">visit_type_macro</a>(&mut self, i: &'ast <a href="../struct.TypeMacro.html" class="struct"
title="struct verus_syn::TypeMacro">TypeMacro</a>)

</div>

<div id="method.visit_type_never" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1029-1031"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_never" class="fn">visit_type_never</a>(&mut self, i: &'ast <a href="../struct.TypeNever.html" class="struct"
title="struct verus_syn::TypeNever">TypeNever</a>)

</div>

<div id="method.visit_type_param" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1034-1036"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param" class="fn">visit_type_param</a>(&mut self, i: &'ast <a href="../struct.TypeParam.html" class="struct"
title="struct verus_syn::TypeParam">TypeParam</a>)

</div>

<div id="method.visit_type_param_bound" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1039-1041"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_bound"
class="fn">visit_type_param_bound</a>(&mut self, i: &'ast <a href="../enum.TypeParamBound.html" class="enum"
title="enum verus_syn::TypeParamBound">TypeParamBound</a>)

</div>

<div id="method.visit_type_paren" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1044-1046"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_paren" class="fn">visit_type_paren</a>(&mut self, i: &'ast <a href="../struct.TypeParen.html" class="struct"
title="struct verus_syn::TypeParen">TypeParen</a>)

</div>

<div id="method.visit_type_path" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1049-1051"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_path" class="fn">visit_type_path</a>(&mut self, i: &'ast <a href="../struct.TypePath.html" class="struct"
title="struct verus_syn::TypePath">TypePath</a>)

</div>

<div id="method.visit_type_ptr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1054-1056"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_ptr" class="fn">visit_type_ptr</a>(&mut self, i: &'ast <a href="../struct.TypePtr.html" class="struct"
title="struct verus_syn::TypePtr">TypePtr</a>)

</div>

<div id="method.visit_type_reference" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1059-1061"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_reference"
class="fn">visit_type_reference</a>(&mut self, i: &'ast <a href="../struct.TypeReference.html" class="struct"
title="struct verus_syn::TypeReference">TypeReference</a>)

</div>

<div id="method.visit_type_slice" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1064-1066"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_slice" class="fn">visit_type_slice</a>(&mut self, i: &'ast <a href="../struct.TypeSlice.html" class="struct"
title="struct verus_syn::TypeSlice">TypeSlice</a>)

</div>

<div id="method.visit_type_trait_object" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1069-1071"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_trait_object"
class="fn">visit_type_trait_object</a>(&mut self, i: &'ast <a href="../struct.TypeTraitObject.html" class="struct"
title="struct verus_syn::TypeTraitObject">TypeTraitObject</a>)

</div>

<div id="method.visit_type_tuple" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1074-1076"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_tuple" class="fn">visit_type_tuple</a>(&mut self, i: &'ast <a href="../struct.TypeTuple.html" class="struct"
title="struct verus_syn::TypeTuple">TypeTuple</a>)

</div>

<div id="method.visit_un_op" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1079-1081"
class="src rightside">Source</a>

#### fn <a href="#method.visit_un_op" class="fn">visit_un_op</a>(&mut self, i: &'ast <a href="../enum.UnOp.html" class="enum"
title="enum verus_syn::UnOp">UnOp</a>)

</div>

<div id="method.visit_uninterp" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1082-1084"
class="src rightside">Source</a>

#### fn <a href="#method.visit_uninterp" class="fn">visit_uninterp</a>(&mut self, i: &'ast <a href="../struct.Uninterp.html" class="struct"
title="struct verus_syn::Uninterp">Uninterp</a>)

</div>

<div id="method.visit_use_glob" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1087-1089"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_glob" class="fn">visit_use_glob</a>(&mut self, i: &'ast <a href="../struct.UseGlob.html" class="struct"
title="struct verus_syn::UseGlob">UseGlob</a>)

</div>

<div id="method.visit_use_group" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1092-1094"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_group" class="fn">visit_use_group</a>(&mut self, i: &'ast <a href="../struct.UseGroup.html" class="struct"
title="struct verus_syn::UseGroup">UseGroup</a>)

</div>

<div id="method.visit_use_name" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1097-1099"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_name" class="fn">visit_use_name</a>(&mut self, i: &'ast <a href="../struct.UseName.html" class="struct"
title="struct verus_syn::UseName">UseName</a>)

</div>

<div id="method.visit_use_path" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1102-1104"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_path" class="fn">visit_use_path</a>(&mut self, i: &'ast <a href="../struct.UsePath.html" class="struct"
title="struct verus_syn::UsePath">UsePath</a>)

</div>

<div id="method.visit_use_rename" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1107-1109"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_rename" class="fn">visit_use_rename</a>(&mut self, i: &'ast <a href="../struct.UseRename.html" class="struct"
title="struct verus_syn::UseRename">UseRename</a>)

</div>

<div id="method.visit_use_tree" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1112-1114"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_tree" class="fn">visit_use_tree</a>(&mut self, i: &'ast <a href="../enum.UseTree.html" class="enum"
title="enum verus_syn::UseTree">UseTree</a>)

</div>

<div id="method.visit_variadic" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1117-1119"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variadic" class="fn">visit_variadic</a>(&mut self, i: &'ast <a href="../struct.Variadic.html" class="struct"
title="struct verus_syn::Variadic">Variadic</a>)

</div>

<div id="method.visit_variant" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1122-1124"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variant" class="fn">visit_variant</a>(&mut self, i: &'ast <a href="../struct.Variant.html" class="struct"
title="struct verus_syn::Variant">Variant</a>)

</div>

<div id="method.visit_view" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1125-1127"
class="src rightside">Source</a>

#### fn <a href="#method.visit_view" class="fn">visit_view</a>(&mut self, i: &'ast <a href="../struct.View.html" class="struct"
title="struct verus_syn::View">View</a>)

</div>

<div id="method.visit_vis_restricted" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1130-1132"
class="src rightside">Source</a>

#### fn <a href="#method.visit_vis_restricted"
class="fn">visit_vis_restricted</a>(&mut self, i: &'ast <a href="../struct.VisRestricted.html" class="struct"
title="struct verus_syn::VisRestricted">VisRestricted</a>)

</div>

<div id="method.visit_visibility" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1135-1137"
class="src rightside">Source</a>

#### fn <a href="#method.visit_visibility" class="fn">visit_visibility</a>(&mut self, i: &'ast <a href="../enum.Visibility.html" class="enum"
title="enum verus_syn::Visibility">Visibility</a>)

</div>

<div id="method.visit_where_clause" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1140-1142"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_clause" class="fn">visit_where_clause</a>(&mut self, i: &'ast <a href="../struct.WhereClause.html" class="struct"
title="struct verus_syn::WhereClause">WhereClause</a>)

</div>

<div id="method.visit_where_predicate" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1145-1147"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_predicate"
class="fn">visit_where_predicate</a>(&mut self, i: &'ast <a href="../enum.WherePredicate.html" class="enum"
title="enum verus_syn::WherePredicate">WherePredicate</a>)

</div>

<div id="method.visit_with_spec_on_expr" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1148-1150"
class="src rightside">Source</a>

#### fn <a href="#method.visit_with_spec_on_expr"
class="fn">visit_with_spec_on_expr</a>(&mut self, i: &'ast <a href="../struct.WithSpecOnExpr.html" class="struct"
title="struct verus_syn::WithSpecOnExpr">WithSpecOnExpr</a>)

</div>

<div id="method.visit_with_spec_on_fn" class="section method">

<a href="../../src/verus_syn/gen/visit.rs.html#1151-1153"
class="src rightside">Source</a>

#### fn <a href="#method.visit_with_spec_on_fn"
class="fn">visit_with_spec_on_fn</a>(&mut self, i: &'ast <a href="../struct.WithSpecOnFn.html" class="struct"
title="struct verus_syn::WithSpecOnFn">WithSpecOnFn</a>)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
