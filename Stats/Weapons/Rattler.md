[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Rattler

Internal weapon id: `AssaultRifle_LowTier_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 12 | 3 |
| II | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 16 | 3 |
| III | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 20 | 3 |
| IV | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 24 | 3 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001945 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 77.666 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -4 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 16 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00175 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 78.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001556 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 79.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001361 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 80.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 24 | 3 |
| Incendiary Rounds | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 24 | 3 |
| More Reload | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 24 | 3 |
| More Reload + Drum Mag | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 64 | 3 |
| More Reload + Drum Mag + Incendiary Rounds | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 64 | 3 |
| More Reload + Incendiary Rounds | 9 | 1 | 9 | 2 | 1 | 1 | 500 | 24 | 3 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 80.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Item_AssaultRifle_LowTier_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/DA_Item_AssaultRifle_LowTier_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 2 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json |
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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 80.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 4 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 2 |
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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 80.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload + Drum Mag

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload_DrumMag |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload + Drum Mag |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 64 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 4 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Drum Mag

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_DrumMag |
| Name | Drum Mag |
| Description | Significantly increases magazine capacity by attaching a drum mag. However, it must still be reloaded a couple of bullets at time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_DrumMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 40 |
| Addmultiply | 1 |
| Multiply | 1 |

**Zoomspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 55.233 |
| Stability | 67.137 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 48 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload + Drum Mag + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload + Drum Mag + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 64 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 4 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Drum Mag

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_DrumMag |
| Name | Drum Mag |
| Description | Significantly increases magazine capacity by attaching a drum mag. However, it must still be reloaded a couple of bullets at time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_DrumMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 40 |
| Addmultiply | 1 |
| Multiply | 1 |

**Zoomspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Basedispersion**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json |
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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 55.233 |
| Stability | 67.137 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 48 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Basedispersion

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.5 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — More Reload + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | More Reload + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000681 |
| Base partial-reload duration, seconds | — |
| Uses shell/looping reload | Yes |
| Base shell-reload entry, seconds | 0.8 |
| Base shell-reload loop, seconds | 0.5 |
| Base shell-reload exit, seconds | 0.2 |
| Shells loaded per loop | 4 |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9 | 9 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.6 | 3.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 13.5 | 13.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 10.8 | 10.8 |

##### Upgrades

###### More Reload

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_MoreReload |
| Name | More Reload |
| Description | Increases the number of bullets loaded at a time, reducing reload time. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Loopingreloadamount**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json |
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
| Damage | 9 |
| Fire rate | 33.333 |
| Range | 56.061 |
| Stability | 80.166 |
| Agility | 54.183 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Loopingreloadamount

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | AssaultRifle_LowTier_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Item_AssaultRifle_LowTier_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Item_AssaultRifle_LowTier_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/DA_Item_AssaultRifle_LowTier_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/DA_Item_AssaultRifle_LowTier_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/DA_Item_AssaultRifle_LowTier_01_MoreReload_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_DrumMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_DrumMag.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json)
- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json)

</details>
