# Burletta

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `Pistol_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_Item_Pistol_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/DA_Item_Pistol_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_WeaponQualitySet_Pistol_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/BP_Projectile_Pistol_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 10 |
| Headshot multiplier | 2.5× |
| ARC armor multiplier | 0.2× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 500 |
| Magazine | 12 |
| Reload stat (s) | 3 |
| Cooldown (s) | 0 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0.1× |
| Durability burn rate | 0.001531 |
| Partial-reload base duration (s) | 1.4 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate |
| --- | --- | --- |
| II | −0.5 | −0.000153 |
| III | −1 | −0.000306 |
| IV | −1.5 | −0.000459 |

### Amplified

Amplified default uses Level IV. Changes include Durability burn rate **−0.000536**.

[Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/BP_Item_Pistol_01_Ascended.json)

Changes are relative to the Amplified default. Where an upgrade has a prerequisite, its row includes the prerequisite’s changes.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Burst Fire | Fire rate (RPM) **+400**, Cooldown (s) **+0.25**, Firing mode **Burst**, Shots per burst **+2** | Makes the weapon fire in a burst. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_Burst.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_Burst.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst.json) |
| Full-Auto | Body damage / projectile **−2**, Headshot multiplier **−1×**, Fire rate (RPM) **+300**, Firing mode **Full-auto**, +100% vertical recoil, +50% horizontal recoil, +50% base dispersion, +200% max firing dispersion, +200% dispersion recovery speed, −50% ADS dispersion scale | Makes the weapon fully automatic, at the cost of accuracy and stability. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_FullAuto.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_FullAuto.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_FullAuto.json) |
| Sprint Shooting | — | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_SprintShooting.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_SprintShooting.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_SprintShooting.json) |
| Increased Burst (requires Burst Fire) | Fire rate (RPM) **+600**, Magazine **+3**, Cooldown (s) **+0.25**, Firing mode **Burst**, Shots per burst **+4** | Increases the number of projectiles fired within a burst. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/DA_Upgrade_Pistol_01_IncreasedBurst.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_01_IncreasedBurst.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Ascended/Permutations/BP_Item_Pistol_01_Burst_IncreasedBurst.json) |

**Mutually exclusive:** Burst Fire, Full-Auto.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 10 |
| Armor | 0.8 |
| Sturdy | 4 |
| WeakPoint | 15 |
| Critical | 15 |
| Fragile | 12 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_01/Curve_DamageFalloff_Pistol_01.json)
