                state_key = str(curr_state)

                ground_actions = []

                move_turn_actions = [
                    "normal_moveF", "careful_moveF",
                    "normal_TurnCW", "careful_TurnCW",
                    "normal_TurnCCW", "careful_TurnCCW"
                ]
                for a in possible_actions_list:
                    if a in move_turn_actions:
                        ground_actions.append((a, a, {}))

                robot_pos = [curr_state["robot"]["x"], curr_state["robot"]["y"]]
                basket_obj = curr_state.get("basket", None)

                if basket_obj is None:
                    for obj_name, obj_info in objects["object"].items():
                        if robot_pos in obj_info["load_loc"]:
                            ground_actions.append(
                                (f"normal_pick {obj_name}", "normal_pick",
                                 {"object_name": obj_name})
                            )
                            ground_actions.append(
                                (f"careful_pick {obj_name}", "careful_pick",
                                 {"object_name": obj_name})
                            )

                if basket_obj is not None:
                    for goal_name, goal_info in objects["goal"].items():
                        if robot_pos in goal_info["load_loc"]:
                            params = {"object_name": basket_obj,
                                      "goal_name": goal_name}
                            ground_actions.append(
                                (f"normal_place {basket_obj} {goal_name}",
                                 "normal_place", params)
                            )
                            ground_actions.append(
                                (f"careful_place {basket_obj} {goal_name}",
                                 "careful_place", params)
                            )

                if not ground_actions:
                    ground_actions = [(a, a, {}) for a in possible_actions_list]

                if state_key not in q_values:
                    q_values[state_key] = {}
                for q_key, _, _ in ground_actions:
                    if q_key not in q_values[state_key]:
                        q_values[state_key][q_key] = 0.0

                if random.random() < epsilon:
                    idx = random.randrange(len(ground_actions))
                else:
                    qs = [q_values[state_key][q_key] for q_key, _, _ in ground_actions]
                    max_q = max(qs)
                    best_indices = [i for i, qv in enumerate(qs) if qv == max_q]
                    idx = random.choice(best_indices)

                q_key, base_action, action_params = ground_actions[idx]

                success, next_state = self.helper.execute_action(base_action, action_params)

                reward = self.helper.get_reward(curr_state, base_action, next_state)

                next_state_key = str(next_state)
                if next_state_key in q_values and q_values[next_state_key]:
                    max_next_q = max(q_values[next_state_key].values())
                else:
                    max_next_q = 0.0

                old_q = q_values[state_key][q_key]
                new_q = self.get_q_value(self.alpha, self.gamma, reward, old_q, max_next_q)
                q_values[state_key][q_key] = new_q

                cumulative_reward = self.compute_cumulative_reward(
                    cumulative_reward, self.gamma, step, reward
                )

                curr_state = next_state

                step = step + 1
            self.write_to_file(self.file_path, i, self.alpha, epsilon, cumulative_reward, step, self.helper.is_terminal_state(curr_state))
            self.helper.reset_world()
        return q_values
