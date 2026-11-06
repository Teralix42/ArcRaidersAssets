# Weapon mechanics

[Weapons](README.md) · [ARC damage model](../ARC/Damage_Model.md) · [Shields](../Shields/)

Stats come from the Steam 2.4 weapon blueprints, inherited defaults, level modifiers and upgrade assets. Each weapon page links its game files.

### Damage and firing

- Body damage uses a 1× hit before falloff and shields. Headshots use the listed multiplier. ARC armor and weak points have their own multipliers.
- Projectiles per shot counts simultaneous projectiles, such as pellets. Shots per burst counts consecutive shots. Configured RPM is the firing-rate setting, with separate timers for trigger delays, bursts, bolt cycling, charging and reloads.
- Damage falloff lists the curve's control points. Explosions and burning have separate targeting, damage and timing.
- Incendiary Rounds adds **0.5 thermal damage every 0.1 s**, with a configured **2 s** duration and **one-stack limit** per target. [Burning effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning_Small.json)

### Levels and Amplified upgrades

- Level II–IV changes are relative to Level I. Amplified default changes are relative to Level IV, or Standard for weapons without levels. Individual upgrades are relative to the Amplified default; prerequisite changes are included where required.
- Stat changes include the numeric timing and damage changes. UI scores describe the inventory bars; they are separate from damage, RPM and seconds. A scope's zoom modifier fraction is a game setting.
- The game selects cached modifiers when `bHasGeneratedBakedModifiers` is enabled. Bettina and Hairpin's Semi-Auto rows give the serialized fire-rate percentage modifier. Their final RPM is omitted because the operation order with their other modifiers has not been established.

### Firing and reload timers

**RPM interval** is `60 / configured RPM`. `UPendulumWeaponNode.GetTimeBetweenShots` selects **CooldownTime for BoltAction** and the **RPM interval for other firing modes**. The bolt-action pages call this selected timer the **fire-action gate**. It is separate from magazine reload duration and charge time.

Ergonomic Bolt switches Jupiter and Osprey from BoltAction to Single and removes the bolt-specific scoped wait. Jupiter's selected gate changes **2 → 1.3333 s (−0.6667 s)**. Osprey's Amplified default inherits the Level IV cooldown, so its selected gate changes **1.2 → 1.3333 s (+0.1333 s)**. These are timer changes, not complete shot-cycle measurements. [Jupiter modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json) · [Osprey modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json)

Jupiter also has **0.75 s initial charge** and **0.2 s extra hipfire windup**, with the extra windup skipped in combat. Its magazine reload setting remains **3 s** with Ergonomic Bolt. [Jupiter blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json) · [Ergonomic Bolt config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_StraightBolt.json)

Bantam sets a **0.06 s hipfire trigger delay**, **0.2 s ADS trigger delay** and **0.25 s ADS settling delay**. These appear separately from its RPM interval. [Bantam blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json)

The input-buffer window defaults to **0.01 s**. Kettle overrides it to **0.03 s**, Bantam to **0.15 s**, Amplified Bettina to **0.1 s** and Amplified Hairpin to **0.2 s**. The code checks `EnableAuthoredBulletInputBuffering()` before clearing buffered requests; its active feature-flag value is not stored in these exports. Input-buffer windows are listed as settings, not added to shot intervals.

The firing code converts durations using `PendulumSimulation::ToTick`, advances timers with `FSimUpdateInput.EngineDt` and clamps negative remaining time to zero in `PendulumPostUpdate`. The exported RPM settings alone do not establish measured in-game cadence.

**Reload stat** comes from `BaseReloadTime` and its modifiers. Partial reloads also use `PartialReloadSteps`, `PartialReloadAnimationScale` and the saved reload stage. Looping reloads use separate entry, loop and exit timings, plus rounds loaded per step. Automatic empty-mag reload has a separate **0.4 s** start delay by default; Ferro overrides it to **0 s**. [Ferro blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json)

<details>
<summary>Game-code rules</summary>

Inherited defaults and timer rules were decoded from `PioneerGame/Script/PrecompiledScript.Cache`, Steam changelist `1450810`.

| Symbol | Behavior |
| --- | --- |
| `UPendulumWeaponNode.GetTimeBetweenShots` | Selects the bolt cooldown or RPM interval by firing mode. |
| `UWeaponItem.PendulumActuallyFire` | Sets the firing timer and runs the bolt-specific cooldown branch. |
| `UWeaponItem.PendulumUpdate` | Advances timers, checks buffered fire and handles the scoped bolt wait. |
| `UWeaponItem.PendulumPostUpdate` | Clamps a negative remaining timer to zero. |
| `UWeaponItem.UWeaponItem` | Sets the input-buffer and automatic-reload defaults. |
| `UDoubleActionFirearm.PendulumStartFire` | Selects the hipfire or ADS trigger delay. |
| `UDoubleActionFirearm.PendulumActuallyFire` | Adds the ADS settling delay. |
| `URailgunItem.PendulumStartFire` | Applies the initial charge and conditional hipfire windup. |
| `UWeaponItem.CalcReloadDurationFromPartialStep` | Calculates the remaining reload from its saved stage. |

</details>
