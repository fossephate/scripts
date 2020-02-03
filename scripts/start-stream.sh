tmux new -d -s stream
tmux select-window -t stream:0
tmux rename-window stream1
tmux new-window
tmux rename-window stream2
tmux select-window -t stream:0
tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v

tmux select-pane -t 0
tmux send-keys 'printf "\033]2;%s\033\\" "account"' 'C-m'
tmux send-keys 'rgio && ./start-account.sh' 'C-m'
tmux select-pane -t 1
tmux send-keys 'printf "\033]2;%s\033\\" "host"' 'C-m'
tmux send-keys 'rgio && ./start-host.sh' 'C-m'
tmux select-pane -t 2
tmux send-keys 'printf "\033]2;%s\033\\" "video"' 'C-m'
tmux send-keys 'rgio && ./start-video.sh' 'C-m'
tmux select-pane -t 3
tmux send-keys 'printf "\033]2;%s\033\\" "watch"' 'C-m'
tmux send-keys 'rgio && npm run watch:prod' 'C-m'

tmux select-window -t 1
tmux rename-window update
tmux select-pane -t 0
tmux send-keys 'printf "\033]2;%s\033\\" "update"' 'C-m'
tmux send-keys 'rgio' 'C-m'

tmux select-window -t stream:0
tmux select-pane -t 0

tmux set -g pane-border-status bottom
tmux set -g pane-border-format '#{pane_index} "#{pane_title}"'

