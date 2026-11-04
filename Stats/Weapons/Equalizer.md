[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Equalizer

Internal weapon id: `Special_BeamRifle_01`. Ammo: **EnergyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unlevelled | 8 | 1 | 8 | 2 | 2.5 | 1.5 | 500 | 50 | 3 |

#### Level Unlevelled

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01 |
| Level | — |
| Level label | Unlevelled |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 50 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000299 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 8 | 8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/DA_Item_Special_BeamRifle_01.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 8 | 1 | 8 | 2 | 2.5 | 1.5 | 500 | 50 | 3 |
| Anti-Weak Point | 8 | 1 | 8 | 2 | 1 | 2.5 | 500 | 50 | 3 |
| Anti-Weak Point + Bigger Mag | 8 | 1 | 8 | 2 | 1 | 2.5 | 500 | 80 | 3 |
| Bigger Mag | 8 | 1 | 8 | 2 | 2.5 | 1.5 | 500 | 80 | 3 |
| Ramping Damage | 8 | 1 | 8 | 2 | 2.5 | 1.5 | 500 | 50 | 3 |
| Ramping Damage + Bigger Mag | 8 | 1 | 8 | 2 | 2.5 | 1.5 | 500 | 80 | 3 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 50 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 8 | 8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/BP_Item_Special_BeamRifle_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/DA_Item_Special_BeamRifle_01_Ascended.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anti-Weak Point

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_AntiWeakPoint |
| Level | 5 |
| Level label | Amplified |
| Variant | Anti-Weak Point |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 2.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 50 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 2.5 | 3.75 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 2.5 | 3.75 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Anti-Weak Point

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_AntiWeakPoint |
| Name | Anti-Weak Point |
| Description | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_AntiWeakPoint.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Aiweakspotdamagemultiplier**

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

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Aiweakspotdamagemultiplier

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint.json, Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Anti-Weak Point + Bigger Mag

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_AntiWeakPoint_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Anti-Weak Point + Bigger Mag |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 2.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 80 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 2.5 | 3.75 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 2.5 | 3.75 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Anti-Weak Point

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_AntiWeakPoint |
| Name | Anti-Weak Point |
| Description | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_AntiWeakPoint.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Aiweakspotdamagemultiplier**

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Aiweakspotdamagemultiplier

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json, Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 80 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 8 | 8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 8 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_BiggerMag.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Ramping Damage

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_RampingDamage |
| Level | 5 |
| Level label | Amplified |
| Variant | Ramping Damage |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 50 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 8 | 8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Ramping Damage

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_RampingDamage |
| Name | Ramping Damage |
| Description | Gradually increases the Equalizer's damage while its laser remains in contact with a valid target. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_RampingDamage.json |
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
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

###### Chargetodamagemultiplier

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/Curve_DamagePerConsecutiveShot_Special_BeamRifle_01_RampingDamage.json |

**Keys**

| X | Y | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.8 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1 | 1.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 12 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Ramping Damage + Bigger Mag

| Identity | Value |
| --- | --- |
| Id | Special_BeamRifle_01_RampingDamage_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Ramping Damage + Bigger Mag |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 500 |
| Firing mode | Auto |
| Burst size stat | 3 |
| Magazine size | 80 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00015 |
| Base partial-reload duration, seconds | 3 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 8 | 8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 18 | 18 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

##### Upgrades

###### Ramping Damage

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_RampingDamage |
| Name | Ramping Damage |
| Description | Gradually increases the Equalizer's damage while its laser remains in contact with a valid target. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_RampingDamage.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| First charge delay s | 1 |
| Damage ramp per hit | 0.1 |
| Damage ramp decay per second | 0.1 |

###### Chargetodamagemultiplier

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/Curve_DamagePerConsecutiveShot_Special_BeamRifle_01_RampingDamage.json |

**Keys**

| X | Y | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.8 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1 | 1.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 12 |
| Fire rate | 33.333 |
| Range | 66.363 |
| Stability | 85.909 |
| Agility | 45.474 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2.066667 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.5 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Special_BeamRifle_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/BP_Item_Special_BeamRifle_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/BP_Item_Special_BeamRifle_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/DA_Item_Special_BeamRifle_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/DA_Item_Special_BeamRifle_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/BP_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_AntiWeakPoint_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Permutations/DA_Item_Special_BeamRifle_01_RampingDamage_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_BeamRifle_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/Curve_DamagePerConsecutiveShot_Special_BeamRifle_01_RampingDamage.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/Curve_DamagePerConsecutiveShot_Special_BeamRifle_01_RampingDamage.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_AntiWeakPoint.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_AntiWeakPoint.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_RampingDamage.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Ascended/Upgrades/DA_Upgrade_Special_BeamRifle_01_RampingDamage.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Item_Special_BeamRifle_01.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/BP_Projectile_Special_BeamRifle_01.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/Curve_DamageFalloff_Special_BeamRifle_01.json)
- [Content/Pioneer/Items/Firearms/Special_BeamRifle_01/DA_Item_Special_BeamRifle_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_BeamRifle_01/DA_Item_Special_BeamRifle_01.json)

</details>
