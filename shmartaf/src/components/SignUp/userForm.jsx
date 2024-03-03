import React, { useState, useEffect } from "react";
import { Form, Input, Checkbox, Button, DatePicker, Select } from "antd";
const { TextArea } = Input;
import { PlusOutlined, MinusOutlined } from "@ant-design/icons";
import { fetchNeeds, fetchSkills } from "../../api";
import { SignUp } from "../../api";
import { createSupabaseClient } from "../../lib/supabaseClient";
import { useNavigate } from "react-router-dom";

const UserForm = () => {
  const [form] = Form.useForm();
  const [isParent, setIsParent] = useState(false);
  const [isBabysitter, setIsBabysitter] = useState(false);
  const [needsData, setNeedsData] = useState([]);
  const [skillsData, setSkillsData] = useState([]);
  const [needsRating, setNeedsRating] = useState({});
  const navigate = useNavigate();
  const getNeedsData = async () => {
    try {
      const needs = await fetchNeeds();
      setNeedsData(needs);

      const intialValuesRating = {};
      needs.forEach((need) => {
        intialValuesRating[need.needname] = 3;
      });
      setNeedsRating(intialValuesRating);
    } catch (error) {
      console.error("Error fetching needs:", error);
    }
  };

  const getSkillsData = async () => {
    try {
      const skills = await fetchSkills();
      setSkillsData(skills);
    } catch (error) {
      console.error("Error fetching skills:", error);
    }
  };

  const handleNeedRatingChange = (id, rating) => {
    setNeedsRating({ ...needsRating, [id]: rating });
  };

  useEffect(() => {
    getNeedsData();
    getSkillsData();
  }, []);

  const handleUserTypeChange = (checkedValues) => {
    setIsParent(checkedValues.includes("parent"));
    setIsBabysitter(checkedValues.includes("babysitter"));
  };

  const handleAddChild = () => {
    const children = form.getFieldValue("children") || [];
    form.setFieldsValue({
      children: [...children, { fullName: "", birthdate: "", needs: [] }],
    });
  };

  const onFinish = async (values) => {
    const supabase = createSupabaseClient();
    console.log("supabase:", supabase);
    const email = values.email;
    const password = values.password;
    const phone = values.phone;

    try {
      const new_user = await supabase.auth.signUp({
        email,
        password,
        phone,
      });
      console.log("new_user:", new_user);
      values.id = new_user.data.user.id;
      values.needs = needsRating;
      console.log("Received values:", values);
      const response = SignUp(values);
      console.log(response);
    } catch (error) {
      console.log("error:", error);
    }

    // Handle form submission logic here
  };

  return (
    <Form form={form} onFinish={onFinish} layout="vertical">
      {/* User Details Section */}
      <Form.Item label="Full Name" name="fullName" required>
        <Input />
      </Form.Item>

      <Form.Item label="Email" name="email" required>
        <Input type="email" />
      </Form.Item>

      <Form.Item label="Password" name="password" required>
        <Input.Password />
      </Form.Item>

      <Form.Item label="City" name="city" required>
        <Input />
      </Form.Item>

      <Form.Item label="Street" name="street" required>
        <Input />
      </Form.Item>

      <Form.Item label="Gender" name="gender" required>
        <Select>
          <Select.Option value="male">Male</Select.Option>
          <Select.Option value="female">Female</Select.Option>
          <Select.Option value="other">Other</Select.Option>
        </Select>
      </Form.Item>

      <Form.Item label="Phone" name="phone" required>
        <Input />
      </Form.Item>
      <Form.Item label="User Type" name="userType" required>
        <Checkbox.Group onChange={handleUserTypeChange}>
          <Checkbox value="parent">Parent</Checkbox>
          <Checkbox value="babysitter">Babysitter</Checkbox>
        </Checkbox.Group>
      </Form.Item>

      {/* Parent Section */}
      {isParent && (
        <>
          <Form.Item
            label="Parent Description"
            name="parentDescription"
            required
          >
            <TextArea />
          </Form.Item>
          <Button
            type="dashed"
            onClick={() => {
              handleAddChild();
            }}
            icon={<PlusOutlined />}
          >
            Add Another Child
          </Button>
          {/* Children Section */}
          <Form.List name="children">
            {(fields, { remove }) => (
              <>
                {fields.map(({ key, name, fieldKey, ...restField }) => (
                  <div key={key}>
                    <Form.Item
                      label={`Child ${
                        fields.length === 1 ? "" : key + 1
                      } Full Name`}
                      {...restField}
                      name={[name, "fullName"]}
                      fieldKey={[fieldKey, "fullName"]}
                      required
                    >
                      <Input />
                    </Form.Item>

                    <Form.Item
                      label={`Child ${
                        fields.length === 1 ? "" : key + 1
                      } Birthdate`}
                      {...restField}
                      name={[name, "birthdate"]}
                      fieldKey={[fieldKey, "birthdate"]}
                      required
                    >
                      <DatePicker />
                    </Form.Item>

                    <Form.Item
                      label={`Child ${
                        fields.length === 1 ? "" : key + 1
                      } Needs`}
                      {...restField}
                      name={[name, "needs"]}
                      fieldKey={[fieldKey, "needs"]}
                      required
                    >
                      <Checkbox.Group>
                        {needsData.map((need) => (
                          <div key={need.id}>
                            <Checkbox value={need.id}>{need.needname}</Checkbox>
                            <Select
                              defaultValue={3} // Default rating
                              onChange={(value) =>
                                handleNeedRatingChange(need.id, value)
                              }
                            >
                              {[1, 2, 3, 4, 5].map((rating) => (
                                <Select.Option key={rating} value={rating}>
                                  {rating}
                                </Select.Option>
                              ))}
                            </Select>
                          </div>
                        ))}
                      </Checkbox.Group>
                    </Form.Item>

                    <Form.Item
                      label={`Child ${
                        fields.length === 1 ? "" : key + 1
                      } gender`}
                      {...restField}
                      name={[name, "gender"]}
                      fieldKey={[fieldKey, "gender"]}
                      required
                    >
                      <Select>
                        <Select.Option value="male">Male</Select.Option>
                        <Select.Option value="female">Female</Select.Option>
                        <Select.Option value="other">Other</Select.Option>
                      </Select>
                    </Form.Item>

                    {/* Only show remove button if there are more than one child */}

                    {fields.length > 1 && (
                      <Button
                        type="dashed"
                        onClick={() => remove(name)}
                        style={{ marginLeft: "8px" }}
                        icon={<MinusOutlined />}
                      >
                        Remove
                      </Button>
                    )}
                  </div>
                ))}
              </>
            )}
          </Form.List>
        </>
      )}

      {/* Babysitter Section */}
      {isBabysitter && (
        <>
          <Form.Item label="Babysitter Skills" name="babysitterSkills" required>
            <Checkbox.Group>
              {skillsData.map((skill) => (
                <Checkbox key={skill.id} value={skill.skillname}>
                  {skill.skillname}
                </Checkbox>
              ))}
            </Checkbox.Group>
          </Form.Item>

          <Form.Item
            label="Babysitter Description"
            name="babysitterDescription"
            required
          >
            <TextArea />
          </Form.Item>
        </>
      )}

      {/* Submit Button */}
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default UserForm;
