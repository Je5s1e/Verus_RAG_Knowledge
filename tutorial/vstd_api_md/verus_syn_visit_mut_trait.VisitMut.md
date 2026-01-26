<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[visit_mut](index.html)

</div>

# Trait <span class="trait">VisitMut</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/gen/visit_mut.rs.html#29-1168"
class="src">Source</a> </span>

</div>

``` rust
pub trait VisitMut {
Show 258 methods    // Provided methods
    fn visit_abi_mut(&mut self, i: &mut Abi) { ... }
    fn visit_angle_bracketed_generic_arguments_mut(
        &mut self,
        i: &mut AngleBracketedGenericArguments,
    ) { ... }
    fn visit_arm_mut(&mut self, i: &mut Arm) { ... }
    fn visit_assert_mut(&mut self, i: &mut Assert) { ... }
    fn visit_assert_forall_mut(&mut self, i: &mut AssertForall) { ... }
    fn visit_assoc_const_mut(&mut self, i: &mut AssocConst) { ... }
    fn visit_assoc_type_mut(&mut self, i: &mut AssocType) { ... }
    fn visit_assume_mut(&mut self, i: &mut Assume) { ... }
    fn visit_assume_specification_mut(&mut self, i: &mut AssumeSpecification) { ... }
    fn visit_attr_style_mut(&mut self, i: &mut AttrStyle) { ... }
    fn visit_attribute_mut(&mut self, i: &mut Attribute) { ... }
    fn visit_attributes_mut(&mut self, i: &mut Vec<Attribute>) { ... }
    fn visit_bare_fn_arg_mut(&mut self, i: &mut BareFnArg) { ... }
    fn visit_bare_variadic_mut(&mut self, i: &mut BareVariadic) { ... }
    fn visit_big_and_mut(&mut self, i: &mut BigAnd) { ... }
    fn visit_big_and_expr_mut(&mut self, i: &mut BigAndExpr) { ... }
    fn visit_big_or_mut(&mut self, i: &mut BigOr) { ... }
    fn visit_big_or_expr_mut(&mut self, i: &mut BigOrExpr) { ... }
    fn visit_bin_op_mut(&mut self, i: &mut BinOp) { ... }
    fn visit_block_mut(&mut self, i: &mut Block) { ... }
    fn visit_bound_lifetimes_mut(&mut self, i: &mut BoundLifetimes) { ... }
    fn visit_broadcast_use_mut(&mut self, i: &mut BroadcastUse) { ... }
    fn visit_captured_param_mut(&mut self, i: &mut CapturedParam) { ... }
    fn visit_closed_mut(&mut self, i: &mut Closed) { ... }
    fn visit_closure_arg_mut(&mut self, i: &mut ClosureArg) { ... }
    fn visit_const_param_mut(&mut self, i: &mut ConstParam) { ... }
    fn visit_constraint_mut(&mut self, i: &mut Constraint) { ... }
    fn visit_data_mut(&mut self, i: &mut Data) { ... }
    fn visit_data_enum_mut(&mut self, i: &mut DataEnum) { ... }
    fn visit_data_mode_mut(&mut self, i: &mut DataMode) { ... }
    fn visit_data_struct_mut(&mut self, i: &mut DataStruct) { ... }
    fn visit_data_union_mut(&mut self, i: &mut DataUnion) { ... }
    fn visit_decreases_mut(&mut self, i: &mut Decreases) { ... }
    fn visit_default_ensures_mut(&mut self, i: &mut DefaultEnsures) { ... }
    fn visit_derive_input_mut(&mut self, i: &mut DeriveInput) { ... }
    fn visit_ensures_mut(&mut self, i: &mut Ensures) { ... }
    fn visit_expr_mut(&mut self, i: &mut Expr) { ... }
    fn visit_expr_array_mut(&mut self, i: &mut ExprArray) { ... }
    fn visit_expr_assign_mut(&mut self, i: &mut ExprAssign) { ... }
    fn visit_expr_async_mut(&mut self, i: &mut ExprAsync) { ... }
    fn visit_expr_await_mut(&mut self, i: &mut ExprAwait) { ... }
    fn visit_expr_binary_mut(&mut self, i: &mut ExprBinary) { ... }
    fn visit_expr_block_mut(&mut self, i: &mut ExprBlock) { ... }
    fn visit_expr_break_mut(&mut self, i: &mut ExprBreak) { ... }
    fn visit_expr_call_mut(&mut self, i: &mut ExprCall) { ... }
    fn visit_expr_cast_mut(&mut self, i: &mut ExprCast) { ... }
    fn visit_expr_closure_mut(&mut self, i: &mut ExprClosure) { ... }
    fn visit_expr_const_mut(&mut self, i: &mut ExprConst) { ... }
    fn visit_expr_continue_mut(&mut self, i: &mut ExprContinue) { ... }
    fn visit_expr_field_mut(&mut self, i: &mut ExprField) { ... }
    fn visit_expr_for_loop_mut(&mut self, i: &mut ExprForLoop) { ... }
    fn visit_expr_get_field_mut(&mut self, i: &mut ExprGetField) { ... }
    fn visit_expr_group_mut(&mut self, i: &mut ExprGroup) { ... }
    fn visit_expr_has_mut(&mut self, i: &mut ExprHas) { ... }
    fn visit_expr_has_not_mut(&mut self, i: &mut ExprHasNot) { ... }
    fn visit_expr_if_mut(&mut self, i: &mut ExprIf) { ... }
    fn visit_expr_index_mut(&mut self, i: &mut ExprIndex) { ... }
    fn visit_expr_infer_mut(&mut self, i: &mut ExprInfer) { ... }
    fn visit_expr_is_mut(&mut self, i: &mut ExprIs) { ... }
    fn visit_expr_is_not_mut(&mut self, i: &mut ExprIsNot) { ... }
    fn visit_expr_let_mut(&mut self, i: &mut ExprLet) { ... }
    fn visit_expr_lit_mut(&mut self, i: &mut ExprLit) { ... }
    fn visit_expr_loop_mut(&mut self, i: &mut ExprLoop) { ... }
    fn visit_expr_macro_mut(&mut self, i: &mut ExprMacro) { ... }
    fn visit_expr_match_mut(&mut self, i: &mut ExprMatch) { ... }
    fn visit_expr_matches_mut(&mut self, i: &mut ExprMatches) { ... }
    fn visit_expr_method_call_mut(&mut self, i: &mut ExprMethodCall) { ... }
    fn visit_expr_paren_mut(&mut self, i: &mut ExprParen) { ... }
    fn visit_expr_path_mut(&mut self, i: &mut ExprPath) { ... }
    fn visit_expr_range_mut(&mut self, i: &mut ExprRange) { ... }
    fn visit_expr_raw_addr_mut(&mut self, i: &mut ExprRawAddr) { ... }
    fn visit_expr_reference_mut(&mut self, i: &mut ExprReference) { ... }
    fn visit_expr_repeat_mut(&mut self, i: &mut ExprRepeat) { ... }
    fn visit_expr_return_mut(&mut self, i: &mut ExprReturn) { ... }
    fn visit_expr_struct_mut(&mut self, i: &mut ExprStruct) { ... }
    fn visit_expr_try_mut(&mut self, i: &mut ExprTry) { ... }
    fn visit_expr_try_block_mut(&mut self, i: &mut ExprTryBlock) { ... }
    fn visit_expr_tuple_mut(&mut self, i: &mut ExprTuple) { ... }
    fn visit_expr_unary_mut(&mut self, i: &mut ExprUnary) { ... }
    fn visit_expr_unsafe_mut(&mut self, i: &mut ExprUnsafe) { ... }
    fn visit_expr_while_mut(&mut self, i: &mut ExprWhile) { ... }
    fn visit_expr_yield_mut(&mut self, i: &mut ExprYield) { ... }
    fn visit_field_mut(&mut self, i: &mut Field) { ... }
    fn visit_field_mutability_mut(&mut self, i: &mut FieldMutability) { ... }
    fn visit_field_pat_mut(&mut self, i: &mut FieldPat) { ... }
    fn visit_field_value_mut(&mut self, i: &mut FieldValue) { ... }
    fn visit_fields_mut(&mut self, i: &mut Fields) { ... }
    fn visit_fields_named_mut(&mut self, i: &mut FieldsNamed) { ... }
    fn visit_fields_unnamed_mut(&mut self, i: &mut FieldsUnnamed) { ... }
    fn visit_file_mut(&mut self, i: &mut File) { ... }
    fn visit_fn_arg_mut(&mut self, i: &mut FnArg) { ... }
    fn visit_fn_arg_kind_mut(&mut self, i: &mut FnArgKind) { ... }
    fn visit_fn_mode_mut(&mut self, i: &mut FnMode) { ... }
    fn visit_fn_proof_arg_mut(&mut self, i: &mut FnProofArg) { ... }
    fn visit_fn_proof_options_mut(&mut self, i: &mut FnProofOptions) { ... }
    fn visit_foreign_item_mut(&mut self, i: &mut ForeignItem) { ... }
    fn visit_foreign_item_fn_mut(&mut self, i: &mut ForeignItemFn) { ... }
    fn visit_foreign_item_macro_mut(&mut self, i: &mut ForeignItemMacro) { ... }
    fn visit_foreign_item_static_mut(&mut self, i: &mut ForeignItemStatic) { ... }
    fn visit_foreign_item_type_mut(&mut self, i: &mut ForeignItemType) { ... }
    fn visit_generic_argument_mut(&mut self, i: &mut GenericArgument) { ... }
    fn visit_generic_param_mut(&mut self, i: &mut GenericParam) { ... }
    fn visit_generics_mut(&mut self, i: &mut Generics) { ... }
    fn visit_global_mut(&mut self, i: &mut Global) { ... }
    fn visit_global_inner_mut(&mut self, i: &mut GlobalInner) { ... }
    fn visit_global_layout_mut(&mut self, i: &mut GlobalLayout) { ... }
    fn visit_global_size_of_mut(&mut self, i: &mut GlobalSizeOf) { ... }
    fn visit_ident_mut(&mut self, i: &mut Ident) { ... }
    fn visit_impl_item_mut(&mut self, i: &mut ImplItem) { ... }
    fn visit_impl_item_const_mut(&mut self, i: &mut ImplItemConst) { ... }
    fn visit_impl_item_fn_mut(&mut self, i: &mut ImplItemFn) { ... }
    fn visit_impl_item_macro_mut(&mut self, i: &mut ImplItemMacro) { ... }
    fn visit_impl_item_type_mut(&mut self, i: &mut ImplItemType) { ... }
    fn visit_impl_restriction_mut(&mut self, i: &mut ImplRestriction) { ... }
    fn visit_index_mut(&mut self, i: &mut Index) { ... }
    fn visit_invariant_mut(&mut self, i: &mut Invariant) { ... }
    fn visit_invariant_ensures_mut(&mut self, i: &mut InvariantEnsures) { ... }
    fn visit_invariant_except_break_mut(&mut self, i: &mut InvariantExceptBreak) { ... }
    fn visit_invariant_name_set_mut(&mut self, i: &mut InvariantNameSet) { ... }
    fn visit_invariant_name_set_any_mut(&mut self, i: &mut InvariantNameSetAny) { ... }
    fn visit_invariant_name_set_list_mut(
        &mut self,
        i: &mut InvariantNameSetList,
    ) { ... }
    fn visit_invariant_name_set_none_mut(
        &mut self,
        i: &mut InvariantNameSetNone,
    ) { ... }
    fn visit_invariant_name_set_set_mut(&mut self, i: &mut InvariantNameSetSet) { ... }
    fn visit_item_mut(&mut self, i: &mut Item) { ... }
    fn visit_item_broadcast_group_mut(&mut self, i: &mut ItemBroadcastGroup) { ... }
    fn visit_item_const_mut(&mut self, i: &mut ItemConst) { ... }
    fn visit_item_enum_mut(&mut self, i: &mut ItemEnum) { ... }
    fn visit_item_extern_crate_mut(&mut self, i: &mut ItemExternCrate) { ... }
    fn visit_item_fn_mut(&mut self, i: &mut ItemFn) { ... }
    fn visit_item_foreign_mod_mut(&mut self, i: &mut ItemForeignMod) { ... }
    fn visit_item_impl_mut(&mut self, i: &mut ItemImpl) { ... }
    fn visit_item_macro_mut(&mut self, i: &mut ItemMacro) { ... }
    fn visit_item_mod_mut(&mut self, i: &mut ItemMod) { ... }
    fn visit_item_static_mut(&mut self, i: &mut ItemStatic) { ... }
    fn visit_item_struct_mut(&mut self, i: &mut ItemStruct) { ... }
    fn visit_item_trait_mut(&mut self, i: &mut ItemTrait) { ... }
    fn visit_item_trait_alias_mut(&mut self, i: &mut ItemTraitAlias) { ... }
    fn visit_item_type_mut(&mut self, i: &mut ItemType) { ... }
    fn visit_item_union_mut(&mut self, i: &mut ItemUnion) { ... }
    fn visit_item_use_mut(&mut self, i: &mut ItemUse) { ... }
    fn visit_label_mut(&mut self, i: &mut Label) { ... }
    fn visit_lifetime_mut(&mut self, i: &mut Lifetime) { ... }
    fn visit_lifetime_param_mut(&mut self, i: &mut LifetimeParam) { ... }
    fn visit_lit_mut(&mut self, i: &mut Lit) { ... }
    fn visit_lit_bool_mut(&mut self, i: &mut LitBool) { ... }
    fn visit_lit_byte_mut(&mut self, i: &mut LitByte) { ... }
    fn visit_lit_byte_str_mut(&mut self, i: &mut LitByteStr) { ... }
    fn visit_lit_cstr_mut(&mut self, i: &mut LitCStr) { ... }
    fn visit_lit_char_mut(&mut self, i: &mut LitChar) { ... }
    fn visit_lit_float_mut(&mut self, i: &mut LitFloat) { ... }
    fn visit_lit_int_mut(&mut self, i: &mut LitInt) { ... }
    fn visit_lit_str_mut(&mut self, i: &mut LitStr) { ... }
    fn visit_local_mut(&mut self, i: &mut Local) { ... }
    fn visit_local_init_mut(&mut self, i: &mut LocalInit) { ... }
    fn visit_loop_spec_mut(&mut self, i: &mut LoopSpec) { ... }
    fn visit_macro_mut(&mut self, i: &mut Macro) { ... }
    fn visit_macro_delimiter_mut(&mut self, i: &mut MacroDelimiter) { ... }
    fn visit_matches_op_expr_mut(&mut self, i: &mut MatchesOpExpr) { ... }
    fn visit_matches_op_token_mut(&mut self, i: &mut MatchesOpToken) { ... }
    fn visit_member_mut(&mut self, i: &mut Member) { ... }
    fn visit_meta_mut(&mut self, i: &mut Meta) { ... }
    fn visit_meta_list_mut(&mut self, i: &mut MetaList) { ... }
    fn visit_meta_name_value_mut(&mut self, i: &mut MetaNameValue) { ... }
    fn visit_mode_mut(&mut self, i: &mut Mode) { ... }
    fn visit_mode_exec_mut(&mut self, i: &mut ModeExec) { ... }
    fn visit_mode_ghost_mut(&mut self, i: &mut ModeGhost) { ... }
    fn visit_mode_proof_mut(&mut self, i: &mut ModeProof) { ... }
    fn visit_mode_proof_axiom_mut(&mut self, i: &mut ModeProofAxiom) { ... }
    fn visit_mode_spec_mut(&mut self, i: &mut ModeSpec) { ... }
    fn visit_mode_spec_checked_mut(&mut self, i: &mut ModeSpecChecked) { ... }
    fn visit_mode_tracked_mut(&mut self, i: &mut ModeTracked) { ... }
    fn visit_open_mut(&mut self, i: &mut Open) { ... }
    fn visit_open_restricted_mut(&mut self, i: &mut OpenRestricted) { ... }
    fn visit_parenthesized_generic_arguments_mut(
        &mut self,
        i: &mut ParenthesizedGenericArguments,
    ) { ... }
    fn visit_pat_mut(&mut self, i: &mut Pat) { ... }
    fn visit_pat_ident_mut(&mut self, i: &mut PatIdent) { ... }
    fn visit_pat_or_mut(&mut self, i: &mut PatOr) { ... }
    fn visit_pat_paren_mut(&mut self, i: &mut PatParen) { ... }
    fn visit_pat_reference_mut(&mut self, i: &mut PatReference) { ... }
    fn visit_pat_rest_mut(&mut self, i: &mut PatRest) { ... }
    fn visit_pat_slice_mut(&mut self, i: &mut PatSlice) { ... }
    fn visit_pat_struct_mut(&mut self, i: &mut PatStruct) { ... }
    fn visit_pat_tuple_mut(&mut self, i: &mut PatTuple) { ... }
    fn visit_pat_tuple_struct_mut(&mut self, i: &mut PatTupleStruct) { ... }
    fn visit_pat_type_mut(&mut self, i: &mut PatType) { ... }
    fn visit_pat_wild_mut(&mut self, i: &mut PatWild) { ... }
    fn visit_path_mut(&mut self, i: &mut Path) { ... }
    fn visit_path_arguments_mut(&mut self, i: &mut PathArguments) { ... }
    fn visit_path_segment_mut(&mut self, i: &mut PathSegment) { ... }
    fn visit_pointer_mutability_mut(&mut self, i: &mut PointerMutability) { ... }
    fn visit_precise_capture_mut(&mut self, i: &mut PreciseCapture) { ... }
    fn visit_predicate_lifetime_mut(&mut self, i: &mut PredicateLifetime) { ... }
    fn visit_predicate_type_mut(&mut self, i: &mut PredicateType) { ... }
    fn visit_prover_mut(&mut self, i: &mut Prover) { ... }
    fn visit_publish_mut(&mut self, i: &mut Publish) { ... }
    fn visit_qself_mut(&mut self, i: &mut QSelf) { ... }
    fn visit_range_limits_mut(&mut self, i: &mut RangeLimits) { ... }
    fn visit_receiver_mut(&mut self, i: &mut Receiver) { ... }
    fn visit_recommends_mut(&mut self, i: &mut Recommends) { ... }
    fn visit_requires_mut(&mut self, i: &mut Requires) { ... }
    fn visit_return_type_mut(&mut self, i: &mut ReturnType) { ... }
    fn visit_returns_mut(&mut self, i: &mut Returns) { ... }
    fn visit_reveal_hide_mut(&mut self, i: &mut RevealHide) { ... }
    fn visit_signature_mut(&mut self, i: &mut Signature) { ... }
    fn visit_signature_decreases_mut(&mut self, i: &mut SignatureDecreases) { ... }
    fn visit_signature_invariants_mut(&mut self, i: &mut SignatureInvariants) { ... }
    fn visit_signature_spec_mut(&mut self, i: &mut SignatureSpec) { ... }
    fn visit_signature_spec_attr_mut(&mut self, i: &mut SignatureSpecAttr) { ... }
    fn visit_signature_unwind_mut(&mut self, i: &mut SignatureUnwind) { ... }
    fn visit_span_mut(&mut self, i: &mut Span) { ... }
    fn visit_specification_mut(&mut self, i: &mut Specification) { ... }
    fn visit_static_mutability_mut(&mut self, i: &mut StaticMutability) { ... }
    fn visit_stmt_mut(&mut self, i: &mut Stmt) { ... }
    fn visit_stmt_macro_mut(&mut self, i: &mut StmtMacro) { ... }
    fn visit_token_stream_mut(&mut self, i: &mut TokenStream) { ... }
    fn visit_trait_bound_mut(&mut self, i: &mut TraitBound) { ... }
    fn visit_trait_bound_modifier_mut(&mut self, i: &mut TraitBoundModifier) { ... }
    fn visit_trait_item_mut(&mut self, i: &mut TraitItem) { ... }
    fn visit_trait_item_const_mut(&mut self, i: &mut TraitItemConst) { ... }
    fn visit_trait_item_fn_mut(&mut self, i: &mut TraitItemFn) { ... }
    fn visit_trait_item_macro_mut(&mut self, i: &mut TraitItemMacro) { ... }
    fn visit_trait_item_type_mut(&mut self, i: &mut TraitItemType) { ... }
    fn visit_type_mut(&mut self, i: &mut Type) { ... }
    fn visit_type_array_mut(&mut self, i: &mut TypeArray) { ... }
    fn visit_type_bare_fn_mut(&mut self, i: &mut TypeBareFn) { ... }
    fn visit_type_fn_proof_mut(&mut self, i: &mut TypeFnProof) { ... }
    fn visit_type_fn_spec_mut(&mut self, i: &mut TypeFnSpec) { ... }
    fn visit_type_group_mut(&mut self, i: &mut TypeGroup) { ... }
    fn visit_type_impl_trait_mut(&mut self, i: &mut TypeImplTrait) { ... }
    fn visit_type_infer_mut(&mut self, i: &mut TypeInfer) { ... }
    fn visit_type_macro_mut(&mut self, i: &mut TypeMacro) { ... }
    fn visit_type_never_mut(&mut self, i: &mut TypeNever) { ... }
    fn visit_type_param_mut(&mut self, i: &mut TypeParam) { ... }
    fn visit_type_param_bound_mut(&mut self, i: &mut TypeParamBound) { ... }
    fn visit_type_paren_mut(&mut self, i: &mut TypeParen) { ... }
    fn visit_type_path_mut(&mut self, i: &mut TypePath) { ... }
    fn visit_type_ptr_mut(&mut self, i: &mut TypePtr) { ... }
    fn visit_type_reference_mut(&mut self, i: &mut TypeReference) { ... }
    fn visit_type_slice_mut(&mut self, i: &mut TypeSlice) { ... }
    fn visit_type_trait_object_mut(&mut self, i: &mut TypeTraitObject) { ... }
    fn visit_type_tuple_mut(&mut self, i: &mut TypeTuple) { ... }
    fn visit_un_op_mut(&mut self, i: &mut UnOp) { ... }
    fn visit_uninterp_mut(&mut self, i: &mut Uninterp) { ... }
    fn visit_use_glob_mut(&mut self, i: &mut UseGlob) { ... }
    fn visit_use_group_mut(&mut self, i: &mut UseGroup) { ... }
    fn visit_use_name_mut(&mut self, i: &mut UseName) { ... }
    fn visit_use_path_mut(&mut self, i: &mut UsePath) { ... }
    fn visit_use_rename_mut(&mut self, i: &mut UseRename) { ... }
    fn visit_use_tree_mut(&mut self, i: &mut UseTree) { ... }
    fn visit_variadic_mut(&mut self, i: &mut Variadic) { ... }
    fn visit_variant_mut(&mut self, i: &mut Variant) { ... }
    fn visit_view_mut(&mut self, i: &mut View) { ... }
    fn visit_vis_restricted_mut(&mut self, i: &mut VisRestricted) { ... }
    fn visit_visibility_mut(&mut self, i: &mut Visibility) { ... }
    fn visit_where_clause_mut(&mut self, i: &mut WhereClause) { ... }
    fn visit_where_predicate_mut(&mut self, i: &mut WherePredicate) { ... }
    fn visit_with_spec_on_expr_mut(&mut self, i: &mut WithSpecOnExpr) { ... }
    fn visit_with_spec_on_fn_mut(&mut self, i: &mut WithSpecOnFn) { ... }
}
```

Expand description

<div class="docblock">

Syntax tree traversal to mutate an exclusive borrow of a syntax tree in
place.

See the [module documentation](index.html "mod verus_syn::visit_mut")
for details.

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.visit_abi_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#32-34"
class="src rightside">Source</a>

#### fn <a href="#method.visit_abi_mut" class="fn">visit_abi_mut</a>(&mut self, i: &mut <a href="../struct.Abi.html" class="struct"
title="struct verus_syn::Abi">Abi</a>)

</div>

<div id="method.visit_angle_bracketed_generic_arguments_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#37-42"
class="src rightside">Source</a>

#### fn <a href="#method.visit_angle_bracketed_generic_arguments_mut"
class="fn">visit_angle_bracketed_generic_arguments_mut</a>( &mut self, i: &mut <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct verus_syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>, )

</div>

<div id="method.visit_arm_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#45-47"
class="src rightside">Source</a>

#### fn <a href="#method.visit_arm_mut" class="fn">visit_arm_mut</a>(&mut self, i: &mut <a href="../struct.Arm.html" class="struct"
title="struct verus_syn::Arm">Arm</a>)

</div>

<div id="method.visit_assert_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#48-50"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assert_mut" class="fn">visit_assert_mut</a>(&mut self, i: &mut <a href="../struct.Assert.html" class="struct"
title="struct verus_syn::Assert">Assert</a>)

</div>

<div id="method.visit_assert_forall_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#51-53"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assert_forall_mut"
class="fn">visit_assert_forall_mut</a>(&mut self, i: &mut <a href="../struct.AssertForall.html" class="struct"
title="struct verus_syn::AssertForall">AssertForall</a>)

</div>

<div id="method.visit_assoc_const_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#56-58"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_const_mut"
class="fn">visit_assoc_const_mut</a>(&mut self, i: &mut <a href="../struct.AssocConst.html" class="struct"
title="struct verus_syn::AssocConst">AssocConst</a>)

</div>

<div id="method.visit_assoc_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#61-63"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_type_mut"
class="fn">visit_assoc_type_mut</a>(&mut self, i: &mut <a href="../struct.AssocType.html" class="struct"
title="struct verus_syn::AssocType">AssocType</a>)

</div>

<div id="method.visit_assume_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#64-66"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assume_mut" class="fn">visit_assume_mut</a>(&mut self, i: &mut <a href="../struct.Assume.html" class="struct"
title="struct verus_syn::Assume">Assume</a>)

</div>

<div id="method.visit_assume_specification_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#67-69"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assume_specification_mut"
class="fn">visit_assume_specification_mut</a>(&mut self, i: &mut <a href="../struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::AssumeSpecification">AssumeSpecification</a>)

</div>

<div id="method.visit_attr_style_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#72-74"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attr_style_mut"
class="fn">visit_attr_style_mut</a>(&mut self, i: &mut <a href="../enum.AttrStyle.html" class="enum"
title="enum verus_syn::AttrStyle">AttrStyle</a>)

</div>

<div id="method.visit_attribute_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#77-79"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attribute_mut" class="fn">visit_attribute_mut</a>(&mut self, i: &mut <a href="../struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>)

</div>

<div id="method.visit_attributes_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#82-86"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attributes_mut"
class="fn">visit_attributes_mut</a>(&mut self, i: &mut <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<<a href="../struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>\>)

</div>

<div id="method.visit_bare_fn_arg_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#89-91"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_fn_arg_mut"
class="fn">visit_bare_fn_arg_mut</a>(&mut self, i: &mut <a href="../struct.BareFnArg.html" class="struct"
title="struct verus_syn::BareFnArg">BareFnArg</a>)

</div>

<div id="method.visit_bare_variadic_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#94-96"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_variadic_mut"
class="fn">visit_bare_variadic_mut</a>(&mut self, i: &mut <a href="../struct.BareVariadic.html" class="struct"
title="struct verus_syn::BareVariadic">BareVariadic</a>)

</div>

<div id="method.visit_big_and_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#97-99"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_and_mut" class="fn">visit_big_and_mut</a>(&mut self, i: &mut <a href="../struct.BigAnd.html" class="struct"
title="struct verus_syn::BigAnd">BigAnd</a>)

</div>

<div id="method.visit_big_and_expr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#100-102"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_and_expr_mut"
class="fn">visit_big_and_expr_mut</a>(&mut self, i: &mut <a href="../struct.BigAndExpr.html" class="struct"
title="struct verus_syn::BigAndExpr">BigAndExpr</a>)

</div>

<div id="method.visit_big_or_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#103-105"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_or_mut" class="fn">visit_big_or_mut</a>(&mut self, i: &mut <a href="../struct.BigOr.html" class="struct"
title="struct verus_syn::BigOr">BigOr</a>)

</div>

<div id="method.visit_big_or_expr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#106-108"
class="src rightside">Source</a>

#### fn <a href="#method.visit_big_or_expr_mut"
class="fn">visit_big_or_expr_mut</a>(&mut self, i: &mut <a href="../struct.BigOrExpr.html" class="struct"
title="struct verus_syn::BigOrExpr">BigOrExpr</a>)

</div>

<div id="method.visit_bin_op_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#111-113"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bin_op_mut" class="fn">visit_bin_op_mut</a>(&mut self, i: &mut <a href="../enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>)

</div>

<div id="method.visit_block_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#116-118"
class="src rightside">Source</a>

#### fn <a href="#method.visit_block_mut" class="fn">visit_block_mut</a>(&mut self, i: &mut <a href="../struct.Block.html" class="struct"
title="struct verus_syn::Block">Block</a>)

</div>

<div id="method.visit_bound_lifetimes_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#121-123"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bound_lifetimes_mut"
class="fn">visit_bound_lifetimes_mut</a>(&mut self, i: &mut <a href="../struct.BoundLifetimes.html" class="struct"
title="struct verus_syn::BoundLifetimes">BoundLifetimes</a>)

</div>

<div id="method.visit_broadcast_use_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#124-126"
class="src rightside">Source</a>

#### fn <a href="#method.visit_broadcast_use_mut"
class="fn">visit_broadcast_use_mut</a>(&mut self, i: &mut <a href="../struct.BroadcastUse.html" class="struct"
title="struct verus_syn::BroadcastUse">BroadcastUse</a>)

</div>

<div id="method.visit_captured_param_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#129-131"
class="src rightside">Source</a>

#### fn <a href="#method.visit_captured_param_mut"
class="fn">visit_captured_param_mut</a>(&mut self, i: &mut <a href="../enum.CapturedParam.html" class="enum"
title="enum verus_syn::CapturedParam">CapturedParam</a>)

</div>

<div id="method.visit_closed_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#132-134"
class="src rightside">Source</a>

#### fn <a href="#method.visit_closed_mut" class="fn">visit_closed_mut</a>(&mut self, i: &mut <a href="../struct.Closed.html" class="struct"
title="struct verus_syn::Closed">Closed</a>)

</div>

<div id="method.visit_closure_arg_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#135-137"
class="src rightside">Source</a>

#### fn <a href="#method.visit_closure_arg_mut"
class="fn">visit_closure_arg_mut</a>(&mut self, i: &mut <a href="../struct.ClosureArg.html" class="struct"
title="struct verus_syn::ClosureArg">ClosureArg</a>)

</div>

<div id="method.visit_const_param_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#140-142"
class="src rightside">Source</a>

#### fn <a href="#method.visit_const_param_mut"
class="fn">visit_const_param_mut</a>(&mut self, i: &mut <a href="../struct.ConstParam.html" class="struct"
title="struct verus_syn::ConstParam">ConstParam</a>)

</div>

<div id="method.visit_constraint_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#145-147"
class="src rightside">Source</a>

#### fn <a href="#method.visit_constraint_mut"
class="fn">visit_constraint_mut</a>(&mut self, i: &mut <a href="../struct.Constraint.html" class="struct"
title="struct verus_syn::Constraint">Constraint</a>)

</div>

<div id="method.visit_data_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#150-152"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_mut" class="fn">visit_data_mut</a>(&mut self, i: &mut <a href="../enum.Data.html" class="enum"
title="enum verus_syn::Data">Data</a>)

</div>

<div id="method.visit_data_enum_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#155-157"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_enum_mut" class="fn">visit_data_enum_mut</a>(&mut self, i: &mut <a href="../struct.DataEnum.html" class="struct"
title="struct verus_syn::DataEnum">DataEnum</a>)

</div>

<div id="method.visit_data_mode_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#158-160"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_mode_mut" class="fn">visit_data_mode_mut</a>(&mut self, i: &mut <a href="../enum.DataMode.html" class="enum"
title="enum verus_syn::DataMode">DataMode</a>)

</div>

<div id="method.visit_data_struct_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#163-165"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_struct_mut"
class="fn">visit_data_struct_mut</a>(&mut self, i: &mut <a href="../struct.DataStruct.html" class="struct"
title="struct verus_syn::DataStruct">DataStruct</a>)

</div>

<div id="method.visit_data_union_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#168-170"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_union_mut"
class="fn">visit_data_union_mut</a>(&mut self, i: &mut <a href="../struct.DataUnion.html" class="struct"
title="struct verus_syn::DataUnion">DataUnion</a>)

</div>

<div id="method.visit_decreases_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#171-173"
class="src rightside">Source</a>

#### fn <a href="#method.visit_decreases_mut" class="fn">visit_decreases_mut</a>(&mut self, i: &mut <a href="../struct.Decreases.html" class="struct"
title="struct verus_syn::Decreases">Decreases</a>)

</div>

<div id="method.visit_default_ensures_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#174-176"
class="src rightside">Source</a>

#### fn <a href="#method.visit_default_ensures_mut"
class="fn">visit_default_ensures_mut</a>(&mut self, i: &mut <a href="../struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::DefaultEnsures">DefaultEnsures</a>)

</div>

<div id="method.visit_derive_input_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#179-181"
class="src rightside">Source</a>

#### fn <a href="#method.visit_derive_input_mut"
class="fn">visit_derive_input_mut</a>(&mut self, i: &mut <a href="../struct.DeriveInput.html" class="struct"
title="struct verus_syn::DeriveInput">DeriveInput</a>)

</div>

<div id="method.visit_ensures_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#182-184"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ensures_mut" class="fn">visit_ensures_mut</a>(&mut self, i: &mut <a href="../struct.Ensures.html" class="struct"
title="struct verus_syn::Ensures">Ensures</a>)

</div>

<div id="method.visit_expr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#187-189"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_mut" class="fn">visit_expr_mut</a>(&mut self, i: &mut <a href="../enum.Expr.html" class="enum"
title="enum verus_syn::Expr">Expr</a>)

</div>

<div id="method.visit_expr_array_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#192-194"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_array_mut"
class="fn">visit_expr_array_mut</a>(&mut self, i: &mut <a href="../struct.ExprArray.html" class="struct"
title="struct verus_syn::ExprArray">ExprArray</a>)

</div>

<div id="method.visit_expr_assign_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#197-199"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_assign_mut"
class="fn">visit_expr_assign_mut</a>(&mut self, i: &mut <a href="../struct.ExprAssign.html" class="struct"
title="struct verus_syn::ExprAssign">ExprAssign</a>)

</div>

<div id="method.visit_expr_async_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#202-204"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_async_mut"
class="fn">visit_expr_async_mut</a>(&mut self, i: &mut <a href="../struct.ExprAsync.html" class="struct"
title="struct verus_syn::ExprAsync">ExprAsync</a>)

</div>

<div id="method.visit_expr_await_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#207-209"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_await_mut"
class="fn">visit_expr_await_mut</a>(&mut self, i: &mut <a href="../struct.ExprAwait.html" class="struct"
title="struct verus_syn::ExprAwait">ExprAwait</a>)

</div>

<div id="method.visit_expr_binary_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#212-214"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_binary_mut"
class="fn">visit_expr_binary_mut</a>(&mut self, i: &mut <a href="../struct.ExprBinary.html" class="struct"
title="struct verus_syn::ExprBinary">ExprBinary</a>)

</div>

<div id="method.visit_expr_block_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#217-219"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_block_mut"
class="fn">visit_expr_block_mut</a>(&mut self, i: &mut <a href="../struct.ExprBlock.html" class="struct"
title="struct verus_syn::ExprBlock">ExprBlock</a>)

</div>

<div id="method.visit_expr_break_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#222-224"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_break_mut"
class="fn">visit_expr_break_mut</a>(&mut self, i: &mut <a href="../struct.ExprBreak.html" class="struct"
title="struct verus_syn::ExprBreak">ExprBreak</a>)

</div>

<div id="method.visit_expr_call_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#227-229"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_call_mut" class="fn">visit_expr_call_mut</a>(&mut self, i: &mut <a href="../struct.ExprCall.html" class="struct"
title="struct verus_syn::ExprCall">ExprCall</a>)

</div>

<div id="method.visit_expr_cast_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#232-234"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_cast_mut" class="fn">visit_expr_cast_mut</a>(&mut self, i: &mut <a href="../struct.ExprCast.html" class="struct"
title="struct verus_syn::ExprCast">ExprCast</a>)

</div>

<div id="method.visit_expr_closure_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#237-239"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_closure_mut"
class="fn">visit_expr_closure_mut</a>(&mut self, i: &mut <a href="../struct.ExprClosure.html" class="struct"
title="struct verus_syn::ExprClosure">ExprClosure</a>)

</div>

<div id="method.visit_expr_const_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#242-244"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_const_mut"
class="fn">visit_expr_const_mut</a>(&mut self, i: &mut <a href="../struct.ExprConst.html" class="struct"
title="struct verus_syn::ExprConst">ExprConst</a>)

</div>

<div id="method.visit_expr_continue_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#247-249"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_continue_mut"
class="fn">visit_expr_continue_mut</a>(&mut self, i: &mut <a href="../struct.ExprContinue.html" class="struct"
title="struct verus_syn::ExprContinue">ExprContinue</a>)

</div>

<div id="method.visit_expr_field_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#252-254"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_field_mut"
class="fn">visit_expr_field_mut</a>(&mut self, i: &mut <a href="../struct.ExprField.html" class="struct"
title="struct verus_syn::ExprField">ExprField</a>)

</div>

<div id="method.visit_expr_for_loop_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#257-259"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_for_loop_mut"
class="fn">visit_expr_for_loop_mut</a>(&mut self, i: &mut <a href="../struct.ExprForLoop.html" class="struct"
title="struct verus_syn::ExprForLoop">ExprForLoop</a>)

</div>

<div id="method.visit_expr_get_field_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#260-262"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_get_field_mut"
class="fn">visit_expr_get_field_mut</a>(&mut self, i: &mut <a href="../struct.ExprGetField.html" class="struct"
title="struct verus_syn::ExprGetField">ExprGetField</a>)

</div>

<div id="method.visit_expr_group_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#265-267"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_group_mut"
class="fn">visit_expr_group_mut</a>(&mut self, i: &mut <a href="../struct.ExprGroup.html" class="struct"
title="struct verus_syn::ExprGroup">ExprGroup</a>)

</div>

<div id="method.visit_expr_has_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#268-270"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_has_mut" class="fn">visit_expr_has_mut</a>(&mut self, i: &mut <a href="../struct.ExprHas.html" class="struct"
title="struct verus_syn::ExprHas">ExprHas</a>)

</div>

<div id="method.visit_expr_has_not_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#271-273"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_has_not_mut"
class="fn">visit_expr_has_not_mut</a>(&mut self, i: &mut <a href="../struct.ExprHasNot.html" class="struct"
title="struct verus_syn::ExprHasNot">ExprHasNot</a>)

</div>

<div id="method.visit_expr_if_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#276-278"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_if_mut" class="fn">visit_expr_if_mut</a>(&mut self, i: &mut <a href="../struct.ExprIf.html" class="struct"
title="struct verus_syn::ExprIf">ExprIf</a>)

</div>

<div id="method.visit_expr_index_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#281-283"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_index_mut"
class="fn">visit_expr_index_mut</a>(&mut self, i: &mut <a href="../struct.ExprIndex.html" class="struct"
title="struct verus_syn::ExprIndex">ExprIndex</a>)

</div>

<div id="method.visit_expr_infer_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#286-288"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_infer_mut"
class="fn">visit_expr_infer_mut</a>(&mut self, i: &mut <a href="../struct.ExprInfer.html" class="struct"
title="struct verus_syn::ExprInfer">ExprInfer</a>)

</div>

<div id="method.visit_expr_is_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#289-291"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_is_mut" class="fn">visit_expr_is_mut</a>(&mut self, i: &mut <a href="../struct.ExprIs.html" class="struct"
title="struct verus_syn::ExprIs">ExprIs</a>)

</div>

<div id="method.visit_expr_is_not_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#292-294"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_is_not_mut"
class="fn">visit_expr_is_not_mut</a>(&mut self, i: &mut <a href="../struct.ExprIsNot.html" class="struct"
title="struct verus_syn::ExprIsNot">ExprIsNot</a>)

</div>

<div id="method.visit_expr_let_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#297-299"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_let_mut" class="fn">visit_expr_let_mut</a>(&mut self, i: &mut <a href="../struct.ExprLet.html" class="struct"
title="struct verus_syn::ExprLet">ExprLet</a>)

</div>

<div id="method.visit_expr_lit_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#302-304"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_lit_mut" class="fn">visit_expr_lit_mut</a>(&mut self, i: &mut <a href="../struct.ExprLit.html" class="struct"
title="struct verus_syn::ExprLit">ExprLit</a>)

</div>

<div id="method.visit_expr_loop_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#307-309"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_loop_mut" class="fn">visit_expr_loop_mut</a>(&mut self, i: &mut <a href="../struct.ExprLoop.html" class="struct"
title="struct verus_syn::ExprLoop">ExprLoop</a>)

</div>

<div id="method.visit_expr_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#312-314"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_macro_mut"
class="fn">visit_expr_macro_mut</a>(&mut self, i: &mut <a href="../struct.ExprMacro.html" class="struct"
title="struct verus_syn::ExprMacro">ExprMacro</a>)

</div>

<div id="method.visit_expr_match_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#317-319"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_match_mut"
class="fn">visit_expr_match_mut</a>(&mut self, i: &mut <a href="../struct.ExprMatch.html" class="struct"
title="struct verus_syn::ExprMatch">ExprMatch</a>)

</div>

<div id="method.visit_expr_matches_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#320-322"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_matches_mut"
class="fn">visit_expr_matches_mut</a>(&mut self, i: &mut <a href="../struct.ExprMatches.html" class="struct"
title="struct verus_syn::ExprMatches">ExprMatches</a>)

</div>

<div id="method.visit_expr_method_call_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#325-327"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_method_call_mut"
class="fn">visit_expr_method_call_mut</a>(&mut self, i: &mut <a href="../struct.ExprMethodCall.html" class="struct"
title="struct verus_syn::ExprMethodCall">ExprMethodCall</a>)

</div>

<div id="method.visit_expr_paren_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#330-332"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_paren_mut"
class="fn">visit_expr_paren_mut</a>(&mut self, i: &mut <a href="../struct.ExprParen.html" class="struct"
title="struct verus_syn::ExprParen">ExprParen</a>)

</div>

<div id="method.visit_expr_path_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#335-337"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_path_mut" class="fn">visit_expr_path_mut</a>(&mut self, i: &mut <a href="../struct.ExprPath.html" class="struct"
title="struct verus_syn::ExprPath">ExprPath</a>)

</div>

<div id="method.visit_expr_range_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#340-342"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_range_mut"
class="fn">visit_expr_range_mut</a>(&mut self, i: &mut <a href="../struct.ExprRange.html" class="struct"
title="struct verus_syn::ExprRange">ExprRange</a>)

</div>

<div id="method.visit_expr_raw_addr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#345-347"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_raw_addr_mut"
class="fn">visit_expr_raw_addr_mut</a>(&mut self, i: &mut <a href="../struct.ExprRawAddr.html" class="struct"
title="struct verus_syn::ExprRawAddr">ExprRawAddr</a>)

</div>

<div id="method.visit_expr_reference_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#350-352"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_reference_mut"
class="fn">visit_expr_reference_mut</a>(&mut self, i: &mut <a href="../struct.ExprReference.html" class="struct"
title="struct verus_syn::ExprReference">ExprReference</a>)

</div>

<div id="method.visit_expr_repeat_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#355-357"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_repeat_mut"
class="fn">visit_expr_repeat_mut</a>(&mut self, i: &mut <a href="../struct.ExprRepeat.html" class="struct"
title="struct verus_syn::ExprRepeat">ExprRepeat</a>)

</div>

<div id="method.visit_expr_return_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#360-362"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_return_mut"
class="fn">visit_expr_return_mut</a>(&mut self, i: &mut <a href="../struct.ExprReturn.html" class="struct"
title="struct verus_syn::ExprReturn">ExprReturn</a>)

</div>

<div id="method.visit_expr_struct_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#365-367"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_struct_mut"
class="fn">visit_expr_struct_mut</a>(&mut self, i: &mut <a href="../struct.ExprStruct.html" class="struct"
title="struct verus_syn::ExprStruct">ExprStruct</a>)

</div>

<div id="method.visit_expr_try_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#370-372"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_mut" class="fn">visit_expr_try_mut</a>(&mut self, i: &mut <a href="../struct.ExprTry.html" class="struct"
title="struct verus_syn::ExprTry">ExprTry</a>)

</div>

<div id="method.visit_expr_try_block_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#375-377"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_block_mut"
class="fn">visit_expr_try_block_mut</a>(&mut self, i: &mut <a href="../struct.ExprTryBlock.html" class="struct"
title="struct verus_syn::ExprTryBlock">ExprTryBlock</a>)

</div>

<div id="method.visit_expr_tuple_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#380-382"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_tuple_mut"
class="fn">visit_expr_tuple_mut</a>(&mut self, i: &mut <a href="../struct.ExprTuple.html" class="struct"
title="struct verus_syn::ExprTuple">ExprTuple</a>)

</div>

<div id="method.visit_expr_unary_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#385-387"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unary_mut"
class="fn">visit_expr_unary_mut</a>(&mut self, i: &mut <a href="../struct.ExprUnary.html" class="struct"
title="struct verus_syn::ExprUnary">ExprUnary</a>)

</div>

<div id="method.visit_expr_unsafe_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#390-392"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unsafe_mut"
class="fn">visit_expr_unsafe_mut</a>(&mut self, i: &mut <a href="../struct.ExprUnsafe.html" class="struct"
title="struct verus_syn::ExprUnsafe">ExprUnsafe</a>)

</div>

<div id="method.visit_expr_while_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#395-397"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_while_mut"
class="fn">visit_expr_while_mut</a>(&mut self, i: &mut <a href="../struct.ExprWhile.html" class="struct"
title="struct verus_syn::ExprWhile">ExprWhile</a>)

</div>

<div id="method.visit_expr_yield_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#400-402"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_yield_mut"
class="fn">visit_expr_yield_mut</a>(&mut self, i: &mut <a href="../struct.ExprYield.html" class="struct"
title="struct verus_syn::ExprYield">ExprYield</a>)

</div>

<div id="method.visit_field_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#405-407"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mut" class="fn">visit_field_mut</a>(&mut self, i: &mut <a href="../struct.Field.html" class="struct"
title="struct verus_syn::Field">Field</a>)

</div>

<div id="method.visit_field_mutability_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#410-412"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mutability_mut"
class="fn">visit_field_mutability_mut</a>(&mut self, i: &mut <a href="../enum.FieldMutability.html" class="enum"
title="enum verus_syn::FieldMutability">FieldMutability</a>)

</div>

<div id="method.visit_field_pat_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#415-417"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_pat_mut" class="fn">visit_field_pat_mut</a>(&mut self, i: &mut <a href="../struct.FieldPat.html" class="struct"
title="struct verus_syn::FieldPat">FieldPat</a>)

</div>

<div id="method.visit_field_value_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#420-422"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_value_mut"
class="fn">visit_field_value_mut</a>(&mut self, i: &mut <a href="../struct.FieldValue.html" class="struct"
title="struct verus_syn::FieldValue">FieldValue</a>)

</div>

<div id="method.visit_fields_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#425-427"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_mut" class="fn">visit_fields_mut</a>(&mut self, i: &mut <a href="../enum.Fields.html" class="enum"
title="enum verus_syn::Fields">Fields</a>)

</div>

<div id="method.visit_fields_named_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#430-432"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_named_mut"
class="fn">visit_fields_named_mut</a>(&mut self, i: &mut <a href="../struct.FieldsNamed.html" class="struct"
title="struct verus_syn::FieldsNamed">FieldsNamed</a>)

</div>

<div id="method.visit_fields_unnamed_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#435-437"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_unnamed_mut"
class="fn">visit_fields_unnamed_mut</a>(&mut self, i: &mut <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct verus_syn::FieldsUnnamed">FieldsUnnamed</a>)

</div>

<div id="method.visit_file_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#440-442"
class="src rightside">Source</a>

#### fn <a href="#method.visit_file_mut" class="fn">visit_file_mut</a>(&mut self, i: &mut <a href="../struct.File.html" class="struct"
title="struct verus_syn::File">File</a>)

</div>

<div id="method.visit_fn_arg_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#445-447"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg_mut" class="fn">visit_fn_arg_mut</a>(&mut self, i: &mut <a href="../struct.FnArg.html" class="struct"
title="struct verus_syn::FnArg">FnArg</a>)

</div>

<div id="method.visit_fn_arg_kind_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#450-452"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg_kind_mut"
class="fn">visit_fn_arg_kind_mut</a>(&mut self, i: &mut <a href="../enum.FnArgKind.html" class="enum"
title="enum verus_syn::FnArgKind">FnArgKind</a>)

</div>

<div id="method.visit_fn_mode_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#453-455"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_mode_mut" class="fn">visit_fn_mode_mut</a>(&mut self, i: &mut <a href="../enum.FnMode.html" class="enum"
title="enum verus_syn::FnMode">FnMode</a>)

</div>

<div id="method.visit_fn_proof_arg_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#456-458"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_proof_arg_mut"
class="fn">visit_fn_proof_arg_mut</a>(&mut self, i: &mut <a href="../struct.FnProofArg.html" class="struct"
title="struct verus_syn::FnProofArg">FnProofArg</a>)

</div>

<div id="method.visit_fn_proof_options_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#459-461"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_proof_options_mut"
class="fn">visit_fn_proof_options_mut</a>(&mut self, i: &mut <a href="../struct.FnProofOptions.html" class="struct"
title="struct verus_syn::FnProofOptions">FnProofOptions</a>)

</div>

<div id="method.visit_foreign_item_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#464-466"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_mut"
class="fn">visit_foreign_item_mut</a>(&mut self, i: &mut <a href="../enum.ForeignItem.html" class="enum"
title="enum verus_syn::ForeignItem">ForeignItem</a>)

</div>

<div id="method.visit_foreign_item_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#469-471"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_fn_mut"
class="fn">visit_foreign_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemFn.html" class="struct"
title="struct verus_syn::ForeignItemFn">ForeignItemFn</a>)

</div>

<div id="method.visit_foreign_item_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#474-476"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_macro_mut"
class="fn">visit_foreign_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct verus_syn::ForeignItemMacro">ForeignItemMacro</a>)

</div>

<div id="method.visit_foreign_item_static_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#479-481"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_static_mut"
class="fn">visit_foreign_item_static_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct verus_syn::ForeignItemStatic">ForeignItemStatic</a>)

</div>

<div id="method.visit_foreign_item_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#484-486"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_type_mut"
class="fn">visit_foreign_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemType.html" class="struct"
title="struct verus_syn::ForeignItemType">ForeignItemType</a>)

</div>

<div id="method.visit_generic_argument_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#489-491"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_argument_mut"
class="fn">visit_generic_argument_mut</a>(&mut self, i: &mut <a href="../enum.GenericArgument.html" class="enum"
title="enum verus_syn::GenericArgument">GenericArgument</a>)

</div>

<div id="method.visit_generic_param_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#494-496"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_param_mut"
class="fn">visit_generic_param_mut</a>(&mut self, i: &mut <a href="../enum.GenericParam.html" class="enum"
title="enum verus_syn::GenericParam">GenericParam</a>)

</div>

<div id="method.visit_generics_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#499-501"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generics_mut" class="fn">visit_generics_mut</a>(&mut self, i: &mut <a href="../struct.Generics.html" class="struct"
title="struct verus_syn::Generics">Generics</a>)

</div>

<div id="method.visit_global_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#502-504"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_mut" class="fn">visit_global_mut</a>(&mut self, i: &mut <a href="../struct.Global.html" class="struct"
title="struct verus_syn::Global">Global</a>)

</div>

<div id="method.visit_global_inner_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#505-507"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_inner_mut"
class="fn">visit_global_inner_mut</a>(&mut self, i: &mut <a href="../enum.GlobalInner.html" class="enum"
title="enum verus_syn::GlobalInner">GlobalInner</a>)

</div>

<div id="method.visit_global_layout_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#508-510"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_layout_mut"
class="fn">visit_global_layout_mut</a>(&mut self, i: &mut <a href="../struct.GlobalLayout.html" class="struct"
title="struct verus_syn::GlobalLayout">GlobalLayout</a>)

</div>

<div id="method.visit_global_size_of_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#511-513"
class="src rightside">Source</a>

#### fn <a href="#method.visit_global_size_of_mut"
class="fn">visit_global_size_of_mut</a>(&mut self, i: &mut <a href="../struct.GlobalSizeOf.html" class="struct"
title="struct verus_syn::GlobalSizeOf">GlobalSizeOf</a>)

</div>

<div id="method.visit_ident_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#514-516"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ident_mut" class="fn">visit_ident_mut</a>(&mut self, i: &mut <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>)

</div>

<div id="method.visit_impl_item_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#519-521"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_mut" class="fn">visit_impl_item_mut</a>(&mut self, i: &mut <a href="../enum.ImplItem.html" class="enum"
title="enum verus_syn::ImplItem">ImplItem</a>)

</div>

<div id="method.visit_impl_item_const_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#524-526"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_const_mut"
class="fn">visit_impl_item_const_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemConst.html" class="struct"
title="struct verus_syn::ImplItemConst">ImplItemConst</a>)

</div>

<div id="method.visit_impl_item_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#529-531"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_fn_mut"
class="fn">visit_impl_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemFn.html" class="struct"
title="struct verus_syn::ImplItemFn">ImplItemFn</a>)

</div>

<div id="method.visit_impl_item_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#534-536"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_macro_mut"
class="fn">visit_impl_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemMacro.html" class="struct"
title="struct verus_syn::ImplItemMacro">ImplItemMacro</a>)

</div>

<div id="method.visit_impl_item_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#539-541"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_type_mut"
class="fn">visit_impl_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemType.html" class="struct"
title="struct verus_syn::ImplItemType">ImplItemType</a>)

</div>

<div id="method.visit_impl_restriction_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#544-546"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_restriction_mut"
class="fn">visit_impl_restriction_mut</a>(&mut self, i: &mut <a href="../enum.ImplRestriction.html" class="enum"
title="enum verus_syn::ImplRestriction">ImplRestriction</a>)

</div>

<div id="method.visit_index_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#549-551"
class="src rightside">Source</a>

#### fn <a href="#method.visit_index_mut" class="fn">visit_index_mut</a>(&mut self, i: &mut <a href="../struct.Index.html" class="struct"
title="struct verus_syn::Index">Index</a>)

</div>

<div id="method.visit_invariant_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#552-554"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_mut" class="fn">visit_invariant_mut</a>(&mut self, i: &mut <a href="../struct.Invariant.html" class="struct"
title="struct verus_syn::Invariant">Invariant</a>)

</div>

<div id="method.visit_invariant_ensures_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#555-557"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_ensures_mut"
class="fn">visit_invariant_ensures_mut</a>(&mut self, i: &mut <a href="../struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::InvariantEnsures">InvariantEnsures</a>)

</div>

<div id="method.visit_invariant_except_break_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#558-560"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_except_break_mut"
class="fn">visit_invariant_except_break_mut</a>(&mut self, i: &mut <a href="../struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::InvariantExceptBreak">InvariantExceptBreak</a>)

</div>

<div id="method.visit_invariant_name_set_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#561-563"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_mut"
class="fn">visit_invariant_name_set_mut</a>(&mut self, i: &mut <a href="../enum.InvariantNameSet.html" class="enum"
title="enum verus_syn::InvariantNameSet">InvariantNameSet</a>)

</div>

<div id="method.visit_invariant_name_set_any_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#564-566"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_any_mut"
class="fn">visit_invariant_name_set_any_mut</a>(&mut self, i: &mut <a href="../struct.InvariantNameSetAny.html" class="struct"
title="struct verus_syn::InvariantNameSetAny">InvariantNameSetAny</a>)

</div>

<div id="method.visit_invariant_name_set_list_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#567-572"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_list_mut"
class="fn">visit_invariant_name_set_list_mut</a>(&mut self, i: &mut <a href="../struct.InvariantNameSetList.html" class="struct"
title="struct verus_syn::InvariantNameSetList">InvariantNameSetList</a>)

</div>

<div id="method.visit_invariant_name_set_none_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#573-578"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_none_mut"
class="fn">visit_invariant_name_set_none_mut</a>(&mut self, i: &mut <a href="../struct.InvariantNameSetNone.html" class="struct"
title="struct verus_syn::InvariantNameSetNone">InvariantNameSetNone</a>)

</div>

<div id="method.visit_invariant_name_set_set_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#579-581"
class="src rightside">Source</a>

#### fn <a href="#method.visit_invariant_name_set_set_mut"
class="fn">visit_invariant_name_set_set_mut</a>(&mut self, i: &mut <a href="../struct.InvariantNameSetSet.html" class="struct"
title="struct verus_syn::InvariantNameSetSet">InvariantNameSetSet</a>)

</div>

<div id="method.visit_item_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#584-586"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mut" class="fn">visit_item_mut</a>(&mut self, i: &mut <a href="../enum.Item.html" class="enum"
title="enum verus_syn::Item">Item</a>)

</div>

<div id="method.visit_item_broadcast_group_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#587-589"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_broadcast_group_mut"
class="fn">visit_item_broadcast_group_mut</a>(&mut self, i: &mut <a href="../struct.ItemBroadcastGroup.html" class="struct"
title="struct verus_syn::ItemBroadcastGroup">ItemBroadcastGroup</a>)

</div>

<div id="method.visit_item_const_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#592-594"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_const_mut"
class="fn">visit_item_const_mut</a>(&mut self, i: &mut <a href="../struct.ItemConst.html" class="struct"
title="struct verus_syn::ItemConst">ItemConst</a>)

</div>

<div id="method.visit_item_enum_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#597-599"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_enum_mut" class="fn">visit_item_enum_mut</a>(&mut self, i: &mut <a href="../struct.ItemEnum.html" class="struct"
title="struct verus_syn::ItemEnum">ItemEnum</a>)

</div>

<div id="method.visit_item_extern_crate_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#602-604"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_extern_crate_mut"
class="fn">visit_item_extern_crate_mut</a>(&mut self, i: &mut <a href="../struct.ItemExternCrate.html" class="struct"
title="struct verus_syn::ItemExternCrate">ItemExternCrate</a>)

</div>

<div id="method.visit_item_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#607-609"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_fn_mut" class="fn">visit_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ItemFn.html" class="struct"
title="struct verus_syn::ItemFn">ItemFn</a>)

</div>

<div id="method.visit_item_foreign_mod_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#612-614"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_foreign_mod_mut"
class="fn">visit_item_foreign_mod_mut</a>(&mut self, i: &mut <a href="../struct.ItemForeignMod.html" class="struct"
title="struct verus_syn::ItemForeignMod">ItemForeignMod</a>)

</div>

<div id="method.visit_item_impl_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#617-619"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_impl_mut" class="fn">visit_item_impl_mut</a>(&mut self, i: &mut <a href="../struct.ItemImpl.html" class="struct"
title="struct verus_syn::ItemImpl">ItemImpl</a>)

</div>

<div id="method.visit_item_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#622-624"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_macro_mut"
class="fn">visit_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ItemMacro.html" class="struct"
title="struct verus_syn::ItemMacro">ItemMacro</a>)

</div>

<div id="method.visit_item_mod_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#627-629"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mod_mut" class="fn">visit_item_mod_mut</a>(&mut self, i: &mut <a href="../struct.ItemMod.html" class="struct"
title="struct verus_syn::ItemMod">ItemMod</a>)

</div>

<div id="method.visit_item_static_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#632-634"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_static_mut"
class="fn">visit_item_static_mut</a>(&mut self, i: &mut <a href="../struct.ItemStatic.html" class="struct"
title="struct verus_syn::ItemStatic">ItemStatic</a>)

</div>

<div id="method.visit_item_struct_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#637-639"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_struct_mut"
class="fn">visit_item_struct_mut</a>(&mut self, i: &mut <a href="../struct.ItemStruct.html" class="struct"
title="struct verus_syn::ItemStruct">ItemStruct</a>)

</div>

<div id="method.visit_item_trait_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#642-644"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_mut"
class="fn">visit_item_trait_mut</a>(&mut self, i: &mut <a href="../struct.ItemTrait.html" class="struct"
title="struct verus_syn::ItemTrait">ItemTrait</a>)

</div>

<div id="method.visit_item_trait_alias_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#647-649"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_alias_mut"
class="fn">visit_item_trait_alias_mut</a>(&mut self, i: &mut <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct verus_syn::ItemTraitAlias">ItemTraitAlias</a>)

</div>

<div id="method.visit_item_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#652-654"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_type_mut" class="fn">visit_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ItemType.html" class="struct"
title="struct verus_syn::ItemType">ItemType</a>)

</div>

<div id="method.visit_item_union_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#657-659"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_union_mut"
class="fn">visit_item_union_mut</a>(&mut self, i: &mut <a href="../struct.ItemUnion.html" class="struct"
title="struct verus_syn::ItemUnion">ItemUnion</a>)

</div>

<div id="method.visit_item_use_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#662-664"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_use_mut" class="fn">visit_item_use_mut</a>(&mut self, i: &mut <a href="../struct.ItemUse.html" class="struct"
title="struct verus_syn::ItemUse">ItemUse</a>)

</div>

<div id="method.visit_label_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#667-669"
class="src rightside">Source</a>

#### fn <a href="#method.visit_label_mut" class="fn">visit_label_mut</a>(&mut self, i: &mut <a href="../struct.Label.html" class="struct"
title="struct verus_syn::Label">Label</a>)

</div>

<div id="method.visit_lifetime_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#670-672"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_mut" class="fn">visit_lifetime_mut</a>(&mut self, i: &mut <a href="../struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>)

</div>

<div id="method.visit_lifetime_param_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#675-677"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_param_mut"
class="fn">visit_lifetime_param_mut</a>(&mut self, i: &mut <a href="../struct.LifetimeParam.html" class="struct"
title="struct verus_syn::LifetimeParam">LifetimeParam</a>)

</div>

<div id="method.visit_lit_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#678-680"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_mut" class="fn">visit_lit_mut</a>(&mut self, i: &mut <a href="../enum.Lit.html" class="enum"
title="enum verus_syn::Lit">Lit</a>)

</div>

<div id="method.visit_lit_bool_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#681-683"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_bool_mut" class="fn">visit_lit_bool_mut</a>(&mut self, i: &mut <a href="../struct.LitBool.html" class="struct"
title="struct verus_syn::LitBool">LitBool</a>)

</div>

<div id="method.visit_lit_byte_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#684-686"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_mut" class="fn">visit_lit_byte_mut</a>(&mut self, i: &mut <a href="../struct.LitByte.html" class="struct"
title="struct verus_syn::LitByte">LitByte</a>)

</div>

<div id="method.visit_lit_byte_str_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#687-689"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_str_mut"
class="fn">visit_lit_byte_str_mut</a>(&mut self, i: &mut <a href="../struct.LitByteStr.html" class="struct"
title="struct verus_syn::LitByteStr">LitByteStr</a>)

</div>

<div id="method.visit_lit_cstr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#690-692"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_cstr_mut" class="fn">visit_lit_cstr_mut</a>(&mut self, i: &mut <a href="../struct.LitCStr.html" class="struct"
title="struct verus_syn::LitCStr">LitCStr</a>)

</div>

<div id="method.visit_lit_char_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#693-695"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_char_mut" class="fn">visit_lit_char_mut</a>(&mut self, i: &mut <a href="../struct.LitChar.html" class="struct"
title="struct verus_syn::LitChar">LitChar</a>)

</div>

<div id="method.visit_lit_float_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#696-698"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_float_mut" class="fn">visit_lit_float_mut</a>(&mut self, i: &mut <a href="../struct.LitFloat.html" class="struct"
title="struct verus_syn::LitFloat">LitFloat</a>)

</div>

<div id="method.visit_lit_int_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#699-701"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_int_mut" class="fn">visit_lit_int_mut</a>(&mut self, i: &mut <a href="../struct.LitInt.html" class="struct"
title="struct verus_syn::LitInt">LitInt</a>)

</div>

<div id="method.visit_lit_str_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#702-704"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_str_mut" class="fn">visit_lit_str_mut</a>(&mut self, i: &mut <a href="../struct.LitStr.html" class="struct"
title="struct verus_syn::LitStr">LitStr</a>)

</div>

<div id="method.visit_local_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#707-709"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_mut" class="fn">visit_local_mut</a>(&mut self, i: &mut <a href="../struct.Local.html" class="struct"
title="struct verus_syn::Local">Local</a>)

</div>

<div id="method.visit_local_init_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#712-714"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_init_mut"
class="fn">visit_local_init_mut</a>(&mut self, i: &mut <a href="../struct.LocalInit.html" class="struct"
title="struct verus_syn::LocalInit">LocalInit</a>)

</div>

<div id="method.visit_loop_spec_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#715-717"
class="src rightside">Source</a>

#### fn <a href="#method.visit_loop_spec_mut" class="fn">visit_loop_spec_mut</a>(&mut self, i: &mut <a href="../struct.LoopSpec.html" class="struct"
title="struct verus_syn::LoopSpec">LoopSpec</a>)

</div>

<div id="method.visit_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#720-722"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_mut" class="fn">visit_macro_mut</a>(&mut self, i: &mut <a href="../struct.Macro.html" class="struct"
title="struct verus_syn::Macro">Macro</a>)

</div>

<div id="method.visit_macro_delimiter_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#725-727"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_delimiter_mut"
class="fn">visit_macro_delimiter_mut</a>(&mut self, i: &mut <a href="../enum.MacroDelimiter.html" class="enum"
title="enum verus_syn::MacroDelimiter">MacroDelimiter</a>)

</div>

<div id="method.visit_matches_op_expr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#728-730"
class="src rightside">Source</a>

#### fn <a href="#method.visit_matches_op_expr_mut"
class="fn">visit_matches_op_expr_mut</a>(&mut self, i: &mut <a href="../struct.MatchesOpExpr.html" class="struct"
title="struct verus_syn::MatchesOpExpr">MatchesOpExpr</a>)

</div>

<div id="method.visit_matches_op_token_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#731-733"
class="src rightside">Source</a>

#### fn <a href="#method.visit_matches_op_token_mut"
class="fn">visit_matches_op_token_mut</a>(&mut self, i: &mut <a href="../enum.MatchesOpToken.html" class="enum"
title="enum verus_syn::MatchesOpToken">MatchesOpToken</a>)

</div>

<div id="method.visit_member_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#736-738"
class="src rightside">Source</a>

#### fn <a href="#method.visit_member_mut" class="fn">visit_member_mut</a>(&mut self, i: &mut <a href="../enum.Member.html" class="enum"
title="enum verus_syn::Member">Member</a>)

</div>

<div id="method.visit_meta_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#741-743"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_mut" class="fn">visit_meta_mut</a>(&mut self, i: &mut <a href="../enum.Meta.html" class="enum"
title="enum verus_syn::Meta">Meta</a>)

</div>

<div id="method.visit_meta_list_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#746-748"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_list_mut" class="fn">visit_meta_list_mut</a>(&mut self, i: &mut <a href="../struct.MetaList.html" class="struct"
title="struct verus_syn::MetaList">MetaList</a>)

</div>

<div id="method.visit_meta_name_value_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#751-753"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_name_value_mut"
class="fn">visit_meta_name_value_mut</a>(&mut self, i: &mut <a href="../struct.MetaNameValue.html" class="struct"
title="struct verus_syn::MetaNameValue">MetaNameValue</a>)

</div>

<div id="method.visit_mode_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#754-756"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_mut" class="fn">visit_mode_mut</a>(&mut self, i: &mut <a href="../enum.Mode.html" class="enum"
title="enum verus_syn::Mode">Mode</a>)

</div>

<div id="method.visit_mode_exec_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#757-759"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_exec_mut" class="fn">visit_mode_exec_mut</a>(&mut self, i: &mut <a href="../struct.ModeExec.html" class="struct"
title="struct verus_syn::ModeExec">ModeExec</a>)

</div>

<div id="method.visit_mode_ghost_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#760-762"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_ghost_mut"
class="fn">visit_mode_ghost_mut</a>(&mut self, i: &mut <a href="../struct.ModeGhost.html" class="struct"
title="struct verus_syn::ModeGhost">ModeGhost</a>)

</div>

<div id="method.visit_mode_proof_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#763-765"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_proof_mut"
class="fn">visit_mode_proof_mut</a>(&mut self, i: &mut <a href="../struct.ModeProof.html" class="struct"
title="struct verus_syn::ModeProof">ModeProof</a>)

</div>

<div id="method.visit_mode_proof_axiom_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#766-768"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_proof_axiom_mut"
class="fn">visit_mode_proof_axiom_mut</a>(&mut self, i: &mut <a href="../struct.ModeProofAxiom.html" class="struct"
title="struct verus_syn::ModeProofAxiom">ModeProofAxiom</a>)

</div>

<div id="method.visit_mode_spec_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#769-771"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_spec_mut" class="fn">visit_mode_spec_mut</a>(&mut self, i: &mut <a href="../struct.ModeSpec.html" class="struct"
title="struct verus_syn::ModeSpec">ModeSpec</a>)

</div>

<div id="method.visit_mode_spec_checked_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#772-774"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_spec_checked_mut"
class="fn">visit_mode_spec_checked_mut</a>(&mut self, i: &mut <a href="../struct.ModeSpecChecked.html" class="struct"
title="struct verus_syn::ModeSpecChecked">ModeSpecChecked</a>)

</div>

<div id="method.visit_mode_tracked_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#775-777"
class="src rightside">Source</a>

#### fn <a href="#method.visit_mode_tracked_mut"
class="fn">visit_mode_tracked_mut</a>(&mut self, i: &mut <a href="../struct.ModeTracked.html" class="struct"
title="struct verus_syn::ModeTracked">ModeTracked</a>)

</div>

<div id="method.visit_open_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#778-780"
class="src rightside">Source</a>

#### fn <a href="#method.visit_open_mut" class="fn">visit_open_mut</a>(&mut self, i: &mut <a href="../struct.Open.html" class="struct"
title="struct verus_syn::Open">Open</a>)

</div>

<div id="method.visit_open_restricted_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#781-783"
class="src rightside">Source</a>

#### fn <a href="#method.visit_open_restricted_mut"
class="fn">visit_open_restricted_mut</a>(&mut self, i: &mut <a href="../struct.OpenRestricted.html" class="struct"
title="struct verus_syn::OpenRestricted">OpenRestricted</a>)

</div>

<div id="method.visit_parenthesized_generic_arguments_mut"
class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#786-791"
class="src rightside">Source</a>

#### fn <a href="#method.visit_parenthesized_generic_arguments_mut"
class="fn">visit_parenthesized_generic_arguments_mut</a>( &mut self, i: &mut <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct verus_syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>, )

</div>

<div id="method.visit_pat_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#794-796"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_mut" class="fn">visit_pat_mut</a>(&mut self, i: &mut <a href="../enum.Pat.html" class="enum"
title="enum verus_syn::Pat">Pat</a>)

</div>

<div id="method.visit_pat_ident_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#799-801"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_ident_mut" class="fn">visit_pat_ident_mut</a>(&mut self, i: &mut <a href="../struct.PatIdent.html" class="struct"
title="struct verus_syn::PatIdent">PatIdent</a>)

</div>

<div id="method.visit_pat_or_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#804-806"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_or_mut" class="fn">visit_pat_or_mut</a>(&mut self, i: &mut <a href="../struct.PatOr.html" class="struct"
title="struct verus_syn::PatOr">PatOr</a>)

</div>

<div id="method.visit_pat_paren_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#809-811"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_paren_mut" class="fn">visit_pat_paren_mut</a>(&mut self, i: &mut <a href="../struct.PatParen.html" class="struct"
title="struct verus_syn::PatParen">PatParen</a>)

</div>

<div id="method.visit_pat_reference_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#814-816"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_reference_mut"
class="fn">visit_pat_reference_mut</a>(&mut self, i: &mut <a href="../struct.PatReference.html" class="struct"
title="struct verus_syn::PatReference">PatReference</a>)

</div>

<div id="method.visit_pat_rest_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#819-821"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_rest_mut" class="fn">visit_pat_rest_mut</a>(&mut self, i: &mut <a href="../struct.PatRest.html" class="struct"
title="struct verus_syn::PatRest">PatRest</a>)

</div>

<div id="method.visit_pat_slice_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#824-826"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_slice_mut" class="fn">visit_pat_slice_mut</a>(&mut self, i: &mut <a href="../struct.PatSlice.html" class="struct"
title="struct verus_syn::PatSlice">PatSlice</a>)

</div>

<div id="method.visit_pat_struct_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#829-831"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_struct_mut"
class="fn">visit_pat_struct_mut</a>(&mut self, i: &mut <a href="../struct.PatStruct.html" class="struct"
title="struct verus_syn::PatStruct">PatStruct</a>)

</div>

<div id="method.visit_pat_tuple_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#834-836"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_mut" class="fn">visit_pat_tuple_mut</a>(&mut self, i: &mut <a href="../struct.PatTuple.html" class="struct"
title="struct verus_syn::PatTuple">PatTuple</a>)

</div>

<div id="method.visit_pat_tuple_struct_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#839-841"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_struct_mut"
class="fn">visit_pat_tuple_struct_mut</a>(&mut self, i: &mut <a href="../struct.PatTupleStruct.html" class="struct"
title="struct verus_syn::PatTupleStruct">PatTupleStruct</a>)

</div>

<div id="method.visit_pat_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#844-846"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_type_mut" class="fn">visit_pat_type_mut</a>(&mut self, i: &mut <a href="../struct.PatType.html" class="struct"
title="struct verus_syn::PatType">PatType</a>)

</div>

<div id="method.visit_pat_wild_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#849-851"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_wild_mut" class="fn">visit_pat_wild_mut</a>(&mut self, i: &mut <a href="../struct.PatWild.html" class="struct"
title="struct verus_syn::PatWild">PatWild</a>)

</div>

<div id="method.visit_path_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#854-856"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_mut" class="fn">visit_path_mut</a>(&mut self, i: &mut <a href="../struct.Path.html" class="struct"
title="struct verus_syn::Path">Path</a>)

</div>

<div id="method.visit_path_arguments_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#859-861"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_arguments_mut"
class="fn">visit_path_arguments_mut</a>(&mut self, i: &mut <a href="../enum.PathArguments.html" class="enum"
title="enum verus_syn::PathArguments">PathArguments</a>)

</div>

<div id="method.visit_path_segment_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#864-866"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_segment_mut"
class="fn">visit_path_segment_mut</a>(&mut self, i: &mut <a href="../struct.PathSegment.html" class="struct"
title="struct verus_syn::PathSegment">PathSegment</a>)

</div>

<div id="method.visit_pointer_mutability_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#869-871"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pointer_mutability_mut"
class="fn">visit_pointer_mutability_mut</a>(&mut self, i: &mut <a href="../enum.PointerMutability.html" class="enum"
title="enum verus_syn::PointerMutability">PointerMutability</a>)

</div>

<div id="method.visit_precise_capture_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#874-876"
class="src rightside">Source</a>

#### fn <a href="#method.visit_precise_capture_mut"
class="fn">visit_precise_capture_mut</a>(&mut self, i: &mut <a href="../struct.PreciseCapture.html" class="struct"
title="struct verus_syn::PreciseCapture">PreciseCapture</a>)

</div>

<div id="method.visit_predicate_lifetime_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#879-881"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_lifetime_mut"
class="fn">visit_predicate_lifetime_mut</a>(&mut self, i: &mut <a href="../struct.PredicateLifetime.html" class="struct"
title="struct verus_syn::PredicateLifetime">PredicateLifetime</a>)

</div>

<div id="method.visit_predicate_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#884-886"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_type_mut"
class="fn">visit_predicate_type_mut</a>(&mut self, i: &mut <a href="../struct.PredicateType.html" class="struct"
title="struct verus_syn::PredicateType">PredicateType</a>)

</div>

<div id="method.visit_prover_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#887-889"
class="src rightside">Source</a>

#### fn <a href="#method.visit_prover_mut" class="fn">visit_prover_mut</a>(&mut self, i: &mut <a href="../struct.Prover.html" class="struct"
title="struct verus_syn::Prover">Prover</a>)

</div>

<div id="method.visit_publish_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#890-892"
class="src rightside">Source</a>

#### fn <a href="#method.visit_publish_mut" class="fn">visit_publish_mut</a>(&mut self, i: &mut <a href="../enum.Publish.html" class="enum"
title="enum verus_syn::Publish">Publish</a>)

</div>

<div id="method.visit_qself_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#895-897"
class="src rightside">Source</a>

#### fn <a href="#method.visit_qself_mut" class="fn">visit_qself_mut</a>(&mut self, i: &mut <a href="../struct.QSelf.html" class="struct"
title="struct verus_syn::QSelf">QSelf</a>)

</div>

<div id="method.visit_range_limits_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#900-902"
class="src rightside">Source</a>

#### fn <a href="#method.visit_range_limits_mut"
class="fn">visit_range_limits_mut</a>(&mut self, i: &mut <a href="../enum.RangeLimits.html" class="enum"
title="enum verus_syn::RangeLimits">RangeLimits</a>)

</div>

<div id="method.visit_receiver_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#905-907"
class="src rightside">Source</a>

#### fn <a href="#method.visit_receiver_mut" class="fn">visit_receiver_mut</a>(&mut self, i: &mut <a href="../struct.Receiver.html" class="struct"
title="struct verus_syn::Receiver">Receiver</a>)

</div>

<div id="method.visit_recommends_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#908-910"
class="src rightside">Source</a>

#### fn <a href="#method.visit_recommends_mut"
class="fn">visit_recommends_mut</a>(&mut self, i: &mut <a href="../struct.Recommends.html" class="struct"
title="struct verus_syn::Recommends">Recommends</a>)

</div>

<div id="method.visit_requires_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#911-913"
class="src rightside">Source</a>

#### fn <a href="#method.visit_requires_mut" class="fn">visit_requires_mut</a>(&mut self, i: &mut <a href="../struct.Requires.html" class="struct"
title="struct verus_syn::Requires">Requires</a>)

</div>

<div id="method.visit_return_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#916-918"
class="src rightside">Source</a>

#### fn <a href="#method.visit_return_type_mut"
class="fn">visit_return_type_mut</a>(&mut self, i: &mut <a href="../enum.ReturnType.html" class="enum"
title="enum verus_syn::ReturnType">ReturnType</a>)

</div>

<div id="method.visit_returns_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#919-921"
class="src rightside">Source</a>

#### fn <a href="#method.visit_returns_mut" class="fn">visit_returns_mut</a>(&mut self, i: &mut <a href="../struct.Returns.html" class="struct"
title="struct verus_syn::Returns">Returns</a>)

</div>

<div id="method.visit_reveal_hide_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#922-924"
class="src rightside">Source</a>

#### fn <a href="#method.visit_reveal_hide_mut"
class="fn">visit_reveal_hide_mut</a>(&mut self, i: &mut <a href="../struct.RevealHide.html" class="struct"
title="struct verus_syn::RevealHide">RevealHide</a>)

</div>

<div id="method.visit_signature_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#927-929"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_mut" class="fn">visit_signature_mut</a>(&mut self, i: &mut <a href="../struct.Signature.html" class="struct"
title="struct verus_syn::Signature">Signature</a>)

</div>

<div id="method.visit_signature_decreases_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#930-932"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_decreases_mut"
class="fn">visit_signature_decreases_mut</a>(&mut self, i: &mut <a href="../struct.SignatureDecreases.html" class="struct"
title="struct verus_syn::SignatureDecreases">SignatureDecreases</a>)

</div>

<div id="method.visit_signature_invariants_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#933-935"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_invariants_mut"
class="fn">visit_signature_invariants_mut</a>(&mut self, i: &mut <a href="../struct.SignatureInvariants.html" class="struct"
title="struct verus_syn::SignatureInvariants">SignatureInvariants</a>)

</div>

<div id="method.visit_signature_spec_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#936-938"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_spec_mut"
class="fn">visit_signature_spec_mut</a>(&mut self, i: &mut <a href="../struct.SignatureSpec.html" class="struct"
title="struct verus_syn::SignatureSpec">SignatureSpec</a>)

</div>

<div id="method.visit_signature_spec_attr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#939-941"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_spec_attr_mut"
class="fn">visit_signature_spec_attr_mut</a>(&mut self, i: &mut <a href="../struct.SignatureSpecAttr.html" class="struct"
title="struct verus_syn::SignatureSpecAttr">SignatureSpecAttr</a>)

</div>

<div id="method.visit_signature_unwind_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#942-944"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_unwind_mut"
class="fn">visit_signature_unwind_mut</a>(&mut self, i: &mut <a href="../struct.SignatureUnwind.html" class="struct"
title="struct verus_syn::SignatureUnwind">SignatureUnwind</a>)

</div>

<div id="method.visit_span_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#945"
class="src rightside">Source</a>

#### fn <a href="#method.visit_span_mut" class="fn">visit_span_mut</a>(&mut self, i: &mut <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div id="method.visit_specification_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#946-948"
class="src rightside">Source</a>

#### fn <a href="#method.visit_specification_mut"
class="fn">visit_specification_mut</a>(&mut self, i: &mut <a href="../struct.Specification.html" class="struct"
title="struct verus_syn::Specification">Specification</a>)

</div>

<div id="method.visit_static_mutability_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#951-953"
class="src rightside">Source</a>

#### fn <a href="#method.visit_static_mutability_mut"
class="fn">visit_static_mutability_mut</a>(&mut self, i: &mut <a href="../enum.StaticMutability.html" class="enum"
title="enum verus_syn::StaticMutability">StaticMutability</a>)

</div>

<div id="method.visit_stmt_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#956-958"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_mut" class="fn">visit_stmt_mut</a>(&mut self, i: &mut <a href="../enum.Stmt.html" class="enum"
title="enum verus_syn::Stmt">Stmt</a>)

</div>

<div id="method.visit_stmt_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#961-963"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_macro_mut"
class="fn">visit_stmt_macro_mut</a>(&mut self, i: &mut <a href="../struct.StmtMacro.html" class="struct"
title="struct verus_syn::StmtMacro">StmtMacro</a>)

</div>

<div id="method.visit_token_stream_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#964"
class="src rightside">Source</a>

#### fn <a href="#method.visit_token_stream_mut"
class="fn">visit_token_stream_mut</a>(&mut self, i: &mut <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div id="method.visit_trait_bound_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#967-969"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_mut"
class="fn">visit_trait_bound_mut</a>(&mut self, i: &mut <a href="../struct.TraitBound.html" class="struct"
title="struct verus_syn::TraitBound">TraitBound</a>)

</div>

<div id="method.visit_trait_bound_modifier_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#972-974"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_modifier_mut"
class="fn">visit_trait_bound_modifier_mut</a>(&mut self, i: &mut <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum verus_syn::TraitBoundModifier">TraitBoundModifier</a>)

</div>

<div id="method.visit_trait_item_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#977-979"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_mut"
class="fn">visit_trait_item_mut</a>(&mut self, i: &mut <a href="../enum.TraitItem.html" class="enum"
title="enum verus_syn::TraitItem">TraitItem</a>)

</div>

<div id="method.visit_trait_item_const_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#982-984"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_const_mut"
class="fn">visit_trait_item_const_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemConst.html" class="struct"
title="struct verus_syn::TraitItemConst">TraitItemConst</a>)

</div>

<div id="method.visit_trait_item_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#987-989"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_fn_mut"
class="fn">visit_trait_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemFn.html" class="struct"
title="struct verus_syn::TraitItemFn">TraitItemFn</a>)

</div>

<div id="method.visit_trait_item_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#992-994"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_macro_mut"
class="fn">visit_trait_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemMacro.html" class="struct"
title="struct verus_syn::TraitItemMacro">TraitItemMacro</a>)

</div>

<div id="method.visit_trait_item_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#997-999"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_type_mut"
class="fn">visit_trait_item_type_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemType.html" class="struct"
title="struct verus_syn::TraitItemType">TraitItemType</a>)

</div>

<div id="method.visit_type_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1002-1004"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_mut" class="fn">visit_type_mut</a>(&mut self, i: &mut <a href="../enum.Type.html" class="enum"
title="enum verus_syn::Type">Type</a>)

</div>

<div id="method.visit_type_array_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1007-1009"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_array_mut"
class="fn">visit_type_array_mut</a>(&mut self, i: &mut <a href="../struct.TypeArray.html" class="struct"
title="struct verus_syn::TypeArray">TypeArray</a>)

</div>

<div id="method.visit_type_bare_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1012-1014"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_bare_fn_mut"
class="fn">visit_type_bare_fn_mut</a>(&mut self, i: &mut <a href="../struct.TypeBareFn.html" class="struct"
title="struct verus_syn::TypeBareFn">TypeBareFn</a>)

</div>

<div id="method.visit_type_fn_proof_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1015-1017"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_fn_proof_mut"
class="fn">visit_type_fn_proof_mut</a>(&mut self, i: &mut <a href="../struct.TypeFnProof.html" class="struct"
title="struct verus_syn::TypeFnProof">TypeFnProof</a>)

</div>

<div id="method.visit_type_fn_spec_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1018-1020"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_fn_spec_mut"
class="fn">visit_type_fn_spec_mut</a>(&mut self, i: &mut <a href="../struct.TypeFnSpec.html" class="struct"
title="struct verus_syn::TypeFnSpec">TypeFnSpec</a>)

</div>

<div id="method.visit_type_group_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1023-1025"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_group_mut"
class="fn">visit_type_group_mut</a>(&mut self, i: &mut <a href="../struct.TypeGroup.html" class="struct"
title="struct verus_syn::TypeGroup">TypeGroup</a>)

</div>

<div id="method.visit_type_impl_trait_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1028-1030"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_impl_trait_mut"
class="fn">visit_type_impl_trait_mut</a>(&mut self, i: &mut <a href="../struct.TypeImplTrait.html" class="struct"
title="struct verus_syn::TypeImplTrait">TypeImplTrait</a>)

</div>

<div id="method.visit_type_infer_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1033-1035"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_infer_mut"
class="fn">visit_type_infer_mut</a>(&mut self, i: &mut <a href="../struct.TypeInfer.html" class="struct"
title="struct verus_syn::TypeInfer">TypeInfer</a>)

</div>

<div id="method.visit_type_macro_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1038-1040"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_macro_mut"
class="fn">visit_type_macro_mut</a>(&mut self, i: &mut <a href="../struct.TypeMacro.html" class="struct"
title="struct verus_syn::TypeMacro">TypeMacro</a>)

</div>

<div id="method.visit_type_never_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1043-1045"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_never_mut"
class="fn">visit_type_never_mut</a>(&mut self, i: &mut <a href="../struct.TypeNever.html" class="struct"
title="struct verus_syn::TypeNever">TypeNever</a>)

</div>

<div id="method.visit_type_param_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1048-1050"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_mut"
class="fn">visit_type_param_mut</a>(&mut self, i: &mut <a href="../struct.TypeParam.html" class="struct"
title="struct verus_syn::TypeParam">TypeParam</a>)

</div>

<div id="method.visit_type_param_bound_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1053-1055"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_bound_mut"
class="fn">visit_type_param_bound_mut</a>(&mut self, i: &mut <a href="../enum.TypeParamBound.html" class="enum"
title="enum verus_syn::TypeParamBound">TypeParamBound</a>)

</div>

<div id="method.visit_type_paren_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1058-1060"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_paren_mut"
class="fn">visit_type_paren_mut</a>(&mut self, i: &mut <a href="../struct.TypeParen.html" class="struct"
title="struct verus_syn::TypeParen">TypeParen</a>)

</div>

<div id="method.visit_type_path_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1063-1065"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_path_mut" class="fn">visit_type_path_mut</a>(&mut self, i: &mut <a href="../struct.TypePath.html" class="struct"
title="struct verus_syn::TypePath">TypePath</a>)

</div>

<div id="method.visit_type_ptr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1068-1070"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_ptr_mut" class="fn">visit_type_ptr_mut</a>(&mut self, i: &mut <a href="../struct.TypePtr.html" class="struct"
title="struct verus_syn::TypePtr">TypePtr</a>)

</div>

<div id="method.visit_type_reference_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1073-1075"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_reference_mut"
class="fn">visit_type_reference_mut</a>(&mut self, i: &mut <a href="../struct.TypeReference.html" class="struct"
title="struct verus_syn::TypeReference">TypeReference</a>)

</div>

<div id="method.visit_type_slice_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1078-1080"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_slice_mut"
class="fn">visit_type_slice_mut</a>(&mut self, i: &mut <a href="../struct.TypeSlice.html" class="struct"
title="struct verus_syn::TypeSlice">TypeSlice</a>)

</div>

<div id="method.visit_type_trait_object_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1083-1085"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_trait_object_mut"
class="fn">visit_type_trait_object_mut</a>(&mut self, i: &mut <a href="../struct.TypeTraitObject.html" class="struct"
title="struct verus_syn::TypeTraitObject">TypeTraitObject</a>)

</div>

<div id="method.visit_type_tuple_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1088-1090"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_tuple_mut"
class="fn">visit_type_tuple_mut</a>(&mut self, i: &mut <a href="../struct.TypeTuple.html" class="struct"
title="struct verus_syn::TypeTuple">TypeTuple</a>)

</div>

<div id="method.visit_un_op_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1093-1095"
class="src rightside">Source</a>

#### fn <a href="#method.visit_un_op_mut" class="fn">visit_un_op_mut</a>(&mut self, i: &mut <a href="../enum.UnOp.html" class="enum"
title="enum verus_syn::UnOp">UnOp</a>)

</div>

<div id="method.visit_uninterp_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1096-1098"
class="src rightside">Source</a>

#### fn <a href="#method.visit_uninterp_mut" class="fn">visit_uninterp_mut</a>(&mut self, i: &mut <a href="../struct.Uninterp.html" class="struct"
title="struct verus_syn::Uninterp">Uninterp</a>)

</div>

<div id="method.visit_use_glob_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1101-1103"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_glob_mut" class="fn">visit_use_glob_mut</a>(&mut self, i: &mut <a href="../struct.UseGlob.html" class="struct"
title="struct verus_syn::UseGlob">UseGlob</a>)

</div>

<div id="method.visit_use_group_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1106-1108"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_group_mut" class="fn">visit_use_group_mut</a>(&mut self, i: &mut <a href="../struct.UseGroup.html" class="struct"
title="struct verus_syn::UseGroup">UseGroup</a>)

</div>

<div id="method.visit_use_name_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1111-1113"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_name_mut" class="fn">visit_use_name_mut</a>(&mut self, i: &mut <a href="../struct.UseName.html" class="struct"
title="struct verus_syn::UseName">UseName</a>)

</div>

<div id="method.visit_use_path_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1116-1118"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_path_mut" class="fn">visit_use_path_mut</a>(&mut self, i: &mut <a href="../struct.UsePath.html" class="struct"
title="struct verus_syn::UsePath">UsePath</a>)

</div>

<div id="method.visit_use_rename_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1121-1123"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_rename_mut"
class="fn">visit_use_rename_mut</a>(&mut self, i: &mut <a href="../struct.UseRename.html" class="struct"
title="struct verus_syn::UseRename">UseRename</a>)

</div>

<div id="method.visit_use_tree_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1126-1128"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_tree_mut" class="fn">visit_use_tree_mut</a>(&mut self, i: &mut <a href="../enum.UseTree.html" class="enum"
title="enum verus_syn::UseTree">UseTree</a>)

</div>

<div id="method.visit_variadic_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1131-1133"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variadic_mut" class="fn">visit_variadic_mut</a>(&mut self, i: &mut <a href="../struct.Variadic.html" class="struct"
title="struct verus_syn::Variadic">Variadic</a>)

</div>

<div id="method.visit_variant_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1136-1138"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variant_mut" class="fn">visit_variant_mut</a>(&mut self, i: &mut <a href="../struct.Variant.html" class="struct"
title="struct verus_syn::Variant">Variant</a>)

</div>

<div id="method.visit_view_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1139-1141"
class="src rightside">Source</a>

#### fn <a href="#method.visit_view_mut" class="fn">visit_view_mut</a>(&mut self, i: &mut <a href="../struct.View.html" class="struct"
title="struct verus_syn::View">View</a>)

</div>

<div id="method.visit_vis_restricted_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1144-1146"
class="src rightside">Source</a>

#### fn <a href="#method.visit_vis_restricted_mut"
class="fn">visit_vis_restricted_mut</a>(&mut self, i: &mut <a href="../struct.VisRestricted.html" class="struct"
title="struct verus_syn::VisRestricted">VisRestricted</a>)

</div>

<div id="method.visit_visibility_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1149-1151"
class="src rightside">Source</a>

#### fn <a href="#method.visit_visibility_mut"
class="fn">visit_visibility_mut</a>(&mut self, i: &mut <a href="../enum.Visibility.html" class="enum"
title="enum verus_syn::Visibility">Visibility</a>)

</div>

<div id="method.visit_where_clause_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1154-1156"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_clause_mut"
class="fn">visit_where_clause_mut</a>(&mut self, i: &mut <a href="../struct.WhereClause.html" class="struct"
title="struct verus_syn::WhereClause">WhereClause</a>)

</div>

<div id="method.visit_where_predicate_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1159-1161"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_predicate_mut"
class="fn">visit_where_predicate_mut</a>(&mut self, i: &mut <a href="../enum.WherePredicate.html" class="enum"
title="enum verus_syn::WherePredicate">WherePredicate</a>)

</div>

<div id="method.visit_with_spec_on_expr_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1162-1164"
class="src rightside">Source</a>

#### fn <a href="#method.visit_with_spec_on_expr_mut"
class="fn">visit_with_spec_on_expr_mut</a>(&mut self, i: &mut <a href="../struct.WithSpecOnExpr.html" class="struct"
title="struct verus_syn::WithSpecOnExpr">WithSpecOnExpr</a>)

</div>

<div id="method.visit_with_spec_on_fn_mut" class="section method">

<a href="../../src/verus_syn/gen/visit_mut.rs.html#1165-1167"
class="src rightside">Source</a>

#### fn <a href="#method.visit_with_spec_on_fn_mut"
class="fn">visit_with_spec_on_fn_mut</a>(&mut self, i: &mut <a href="../struct.WithSpecOnFn.html" class="struct"
title="struct verus_syn::WithSpecOnFn">WithSpecOnFn</a>)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
