/**
 * Terminal workflow detection for cmux integration.
 *
 * @module worktree/terminal
 */

/**
 * Check if cmux workflow is available (cmux CLI is installed and CMUX env is set).
 */
export function canUseCmuxWorkflow(
	env: Record<string, string | undefined> = process.env,
	resolveExecutable?: (command: string) => string | null | undefined,
	cmuxCommand: string = "cmux",
): boolean {
	// Must have CMUX env var set (means we're in a cmux session)
	if (!env.CMUX) return false

	// Check if cmux CLI is available
	const resolve = resolveExecutable ?? ((cmd: string) => {
		try { return Bun.which(cmd) } catch { return null }
	})
	return !!resolve(cmuxCommand)
}
