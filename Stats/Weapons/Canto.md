[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Canto

Internal weapon id: `SMG_Medium_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 18 | 4 |
| II | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 20 | 3.5 |
| III | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 22 | 3 |
| IV | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 24 | 2.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 18 |
| Reload time stat, seconds | 4 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001275 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 44.084 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001148 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 44.084 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 22 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00102 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 45.084 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000892 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 48.584 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 24 | 2.5 |
| Carbine Conversion | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 765 | 24 | 2.5 |
| Incendiary Rounds | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 24 | 2.5 |
| Incendiary Rounds + Carbine Conversion | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 765 | 24 | 2.5 |
| Incendiary Rounds + Sprint Shooting | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 24 | 2.5 |
| Sprint Shooting | 6.5 | 1 | 6.5 | 1.75 | 0.8 | 1 | 850 | 24 | 2.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 48.584 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Item_SMG_Medium_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/DA_Item_SMG_Medium_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Carbine Conversion

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_Carbine |
| Level | 5 |
| Level label | Amplified |
| Variant | Carbine Conversion |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 765 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Carbine Conversion

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Carbine |
| Name | Carbine Conversion |
| Description | Repurposes the Canto as a carbine, greatly improving stability and accuracy at the cost of agility. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Carbine.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

**Unequiptime**

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Equiptime**

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Zoomrecoilgainmultiplier**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 51 |
| Range | 54.507 |
| Stability | 69.351 |
| Agility | 67.7 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

###### Unequiptime

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Equiptime

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Zoomrecoilgainmultiplier

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_Carbine.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_Carbine.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 48.584 |
| Agility | 75.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds + Carbine Conversion

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds_Carbine |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds + Carbine Conversion |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 765 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

###### Carbine Conversion

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Carbine |
| Name | Carbine Conversion |
| Description | Repurposes the Canto as a carbine, greatly improving stability and accuracy at the cost of agility. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Carbine.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

**Unequiptime**

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Equiptime**

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

**Zoomrecoilgainmultiplier**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 51 |
| Range | 54.507 |
| Stability | 69.351 |
| Agility | 67.7 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

###### Unequiptime

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Equiptime

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Zoomrecoilgainmultiplier

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 48.584 |
| Agility | 80.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | SMG_Medium_01_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6.5 |
| Firearm critical/headshot multiplier | 1.75 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 850 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000446 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6.5 | 6.5 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.08 | 2.08 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.6 | 2.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9.75 | 9.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.8 | 7.8 |

##### Upgrades

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 6.5 |
| Fire rate | 56.667 |
| Range | 50.825 |
| Stability | 48.584 |
| Agility | 80.008 |
| Stealth | 24 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | SMG_Medium_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Item_SMG_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Item_SMG_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/BP_Projectile_SMG_Medium_Incendiary.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/DA_Item_SMG_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/DA_Item_SMG_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/BP_Item_SMG_Medium_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_IncendiaryRounds_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Permutations/DA_Item_SMG_Medium_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SMG_Medium_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Carbine.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_Carbine.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Ascended/Upgrades/DA_Upgrade_SMG_Medium_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Item_SMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_Projectile_SMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/BP_WeaponQualitySet_SMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/Curve_DamageFalloff_SMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_Medium_01/DA_Item_SMG_Medium_01.json)

</details>
