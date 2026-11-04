[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Renegade

Internal weapon id: `BattleRifle_LeverAction_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 45 | 8 | 3.5 |
| II | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 60 | 8 | 3.5 |
| III | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 75 | 8 | 3.5 |
| IV | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 90 | 8 | 3.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003719 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

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
| Damage | 35 |
| Fire rate | 7.5 |
| Range | 68.751 |
| Stability | 87.371 |
| Agility | 42.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 1.2 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | -15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 60 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003347 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

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
| Damage | 35 |
| Fire rate | 9 |
| Range | 68.751 |
| Stability | 85.371 |
| Agility | 43.823 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 75 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002975 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

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
| Damage | 35 |
| Fire rate | 10.5 |
| Range | 68.751 |
| Stability | 83.371 |
| Agility | 45.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.8 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 90 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002603 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

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
| Damage | 35 |
| Fire rate | 12 |
| Range | 68.751 |
| Stability | 80.871 |
| Agility | 46.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.6 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 90 | 8 | 3.5 |
| More Reload | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 90 | 8 | 3.5 |
| More Reload + Scoped | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 90 | 8 | 3.5 |
| Scoped | 35 | 1 | 35 | 2.25 | 0.8 | 1 | 90 | 8 | 3.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 90 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001302 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

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
| Damage | 35 |
| Fire rate | 12 |
| Range | 68.751 |
| Stability | 80.871 |
| Agility | 46.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.6 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/BP_Item_BattleRifle_LeverAction_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/DA_Item_BattleRifle_LeverAction_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_MoreReload |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 90 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001302 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
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
| Damage | 35 |
| Fire rate | 12 |
| Range | 68.751 |
| Stability | 80.871 |
| Agility | 46.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.6 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload + Scoped

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_MoreReload_Scoped |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload + Scoped |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 90 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001302 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Scoped

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Scoped.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.uasset |
| Modifier selection | baked_cache_enabled |

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
| Damage | 35 |
| Fire rate | 12 |
| Range | 74.808 |
| Stability | 77.936 |
| Agility | 46.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.6 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Scoped

| Identity | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Scoped |
| Level | 5 |
| Level label | Amplified |
| Variant | Scoped |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 35 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 35 |
| Firearm critical/headshot multiplier | 2.25 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 90 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001302 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.4 |
| Shells loaded per loop | 1 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 35 | 35 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 11.2 | 11.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 14 | 14 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 52.5 | 52.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 42 | 42 |

##### Upgrades

###### Scoped

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Scoped.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.uasset |
| Modifier selection | baked_cache_enabled |

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
| Damage | 35 |
| Fire rate | 12 |
| Range | 74.808 |
| Stability | 77.936 |
| Agility | 46.323 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1 |
| Multiply | 0.6 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_Scoped.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_Scoped.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_LeverAction_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/BP_Item_BattleRifle_LeverAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/BP_Item_BattleRifle_LeverAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/DA_Item_BattleRifle_LeverAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/DA_Item_BattleRifle_LeverAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_MoreReload_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json)

</details>
