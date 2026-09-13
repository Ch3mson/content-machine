# Accounts

One account is live: [`antigpt/`](antigpt/README.md). Its README is the hub for
the avatar, boards, posts, and commands.

## Folder contract

```text
accounts/{account}/
  README.md            # hub: format, avatar identity, boards table, posts table, commands
  account-brief.md     # audience, POV, product relationship
  avatar/asian-girl-avatar.jpg    # identity lock for fal edits
  boards/              # composition boards (Figure 2 inputs), never posted
  outputs/{stamp}/      # face-swap candidates + contact sheet (gitignored)
  posts/N/
    image.jpg          # clean promoted still
    image_caption.jpg  # captioned render
    caption.md         # status, board, approved copy
  assets/              # fonts, logo
```

Posts are single stills. Promote a review candidate with
`python tools/fal/swap_avatar.py <board> --post N`, then update the posts table
in the account README by hand.
