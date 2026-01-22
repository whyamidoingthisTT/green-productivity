-- ==========================================
-- Seed data for Green Productivity
-- Purpose:
-- - Validate analytics logic
-- - Demonstrate PostgreSQL + SQLAlchemy usage
-- - NOT production data
--
-- Assumes:
-- - Fresh database OR empty tables
-- - Alembic migrations already applied
-- ==========================================

-- Clean existing data (safe for local/dev only)
DELETE FROM focus_sessions;
DELETE FROM tasks;
DELETE FROM daily_reflections;

-- ==========================================
-- Tasks for 2026-01-20
-- ==========================================

INSERT INTO tasks (
    id,
    title,
    difficulty,
    category,
    is_completed,
    task_date,
    created_at,
    updated_at,
    is_deleted
)
VALUES
(
    gen_random_uuid(),
    'Study SQLAlchemy',
    'medium',
    'study',
    TRUE,
    '2026-01-20',
    NOW(), NOW(), FALSE
),
(
    gen_random_uuid(),
    'Read system design notes',
    'hard',
    'study',
    FALSE,
    '2026-01-20',
    NOW(), NOW(), FALSE
),
(
    gen_random_uuid(),
    'Organize daily tasks',
    'easy',
    'personal',
    FALSE,
    '2026-01-20',
    NOW(), NOW(), FALSE
);


-- ==========================================
-- Focus sessions for 2026-01-20
-- ==========================================

INSERT INTO focus_sessions (
    id,
    task_id,
    session_date,
    start_time,
    end_time,
    duration_minutes,
    created_at,
    updated_at,
    is_deleted
)
SELECT
    gen_random_uuid(),
    t.id,
    '2026-01-20',
    '2026-01-20 18:00:00',
    '2026-01-20 19:00:00',
    60,
    NOW(),
    NOW(),
    FALSE
FROM tasks t
LIMIT 1;


-- ==========================================
-- Daily reflection for mood correlation
-- ==========================================

INSERT INTO daily_reflections (
    id,
    date,
    mood,
    energy,
    gratitude_note,
    created_at,
    updated_at,
    is_deleted
)
VALUES (
    gen_random_uuid(),
    '2026-01-20',
    4,
    'medium',
    'Focused well during the evening study session',
    NOW(),
    NOW(),
    FALSE
);


-- ==========================================
-- Verification
-- ==========================================

SELECT task_date, COUNT(*) FROM tasks GROUP BY task_date;
SELECT session_date, SUM(duration_minutes) FROM focus_sessions GROUP BY session_date;
SELECT date, mood FROM daily_reflections;
