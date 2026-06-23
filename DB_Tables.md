### Customer API Implementation Plan (TDD Approach)

Domain Object Fields

┌────────────────┬──────────┬──────────────────────────────┐
│     Field      │   Type   │            Notes             │
├────────────────┼──────────┼──────────────────────────────┤
│ id             │ UUID     │ Auto-generated, unique       │
├────────────────┼──────────┼──────────────────────────────┤
│ name           │ str      │ Customer name                │
├────────────────┼──────────┼──────────────────────────────┤
│ email          │ str      │ Unique email                 │
├────────────────┼──────────┼──────────────────────────────┤
│ phone          │ str      │ Contact number               │
├────────────────┼──────────┼──────────────────────────────┤
│ created_at     │ datetime │ Auto-managed timestamp       │
├────────────────┼──────────┼──────────────────────────────┤
│ created_by     │ int/str  │ User ID who created          │
├────────────────┼──────────┼──────────────────────────────┤
│ updated_at     │ datetime │ Auto-managed timestamp       │
├────────────────┼──────────┼──────────────────────────────┤
│ updated_by     │ int/str  │ User ID who updated          │
├────────────────┼──────────┼──────────────────────────────┤
│ is_active      │ bool     │ Default: true                │
└────────────────┴──────────┴──────────────────────────────┘

