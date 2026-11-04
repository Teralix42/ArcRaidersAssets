[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Jupiter

Internal weapon id: `Special_Railgun_01`. Ammo: **EnergyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unlevelled | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 5 | 3 |

#### Level Unlevelled

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01 |
| Level | — |
| Level label | Unlevelled |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.0045 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 5 |
| Range | 73.417 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/DA_Item_Special_Railgun_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 5 | 3 |
| Bigger Mag | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 10 | 3 |
| Bigger Mag + Scoped | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 10 | 3 |
| Bigger Mag + Scoped + Ergonomic Bolt | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 10 | 3 |
| Bigger Mag + Ergonomic Bolt | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 10 | 3 |
| Scoped | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 5 | 3 |
| Scoped + Ergonomic Bolt | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 5 | 3 |
| Ergonomic Bolt | 60 | 1 | 60 | 2 | 3 | 1.3 | 45 | 5 | 3 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 5 |
| Range | 73.417 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/BP_Item_Special_Railgun_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/DA_Item_Special_Railgun_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 5 |
| Range | 73.417 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Scoped

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag_Scoped |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Scoped |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Scoped

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json |
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

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 5 |
| Range | 78.321 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Scoped + Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag_Scoped_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Scoped + Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Scoped

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 8 |
| Range | 78.321 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 8 |
| Range | 73.417 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Scoped

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped |
| Level | 5 |
| Level label | Amplified |
| Variant | Scoped |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | BoltAction |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Scoped

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json |
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

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 5 |
| Range | 78.321 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Scoped + Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Scoped + Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Scoped

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Scoped |
| Name | Scoped |
| Description | Adds a scope to the weapon, allowing it to be fired from a scoped view. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 8 |
| Range | 78.321 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Ergonomic Bolt

| Identity | Value |
| --- | --- |
| Id | Special_Railgun_01_StraightBolt |
| Level | 5 |
| Level label | Amplified |
| Variant | Ergonomic Bolt |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 60 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 60 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 3 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1.3 |
| Fire rate stat, RPM | 45 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 5 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 2 |
| Durability burn rate stat | 0.00225 |
| Base partial-reload duration, seconds | 3.3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 60 | 60 |
| Armor | 0.6 | 0.4 | 3 | 1 | 1 | 60 | 60 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 24 | 24 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Critical | -0.5 | 1.5 | 1 | 1.3 | 1.95 | 117 | 117 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 72 | 72 |

##### Upgrades

###### Ergonomic Bolt

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_StraightBolt |
| Name | Ergonomic Bolt |
| Description | Ergonomic bolt that allows the user to perform the bolt-action while scoped. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 0.75 |
| Damage multiplier per penetrated hit | 0.75 |
| Extra hipfire windup s | 0.2 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 60 |
| Fire rate | 8 |
| Range | 73.417 |
| Stability | 85.435 |
| Agility | 68.442 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_StraightBolt.json |
| Item | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_StraightBolt.json |
| Quality set | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_Railgun_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/BP_Item_Special_Railgun_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/BP_Item_Special_Railgun_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/DA_Item_Special_Railgun_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/DA_Item_Special_Railgun_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_Scoped_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_BiggerMag_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json)
- [Content/Pioneer/Items/Firearms/Special_Railgun_01/DA_Item_Special_Railgun_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/DA_Item_Special_Railgun_01.json)

</details>
